from fastapi import FastAPI, Depends, HTTPException #API depends para o front e HTTP para dar retorno
from fastapi.middleware.cors import CORSMiddleware #habilitar conversa do front com back
from pydantic import BaseModel #validação de dados
from sqlalchemy import create_engine, Column, Integer, String, DateTime #Banco de dados
from sqlalchemy.orm import sessionmaker, declarative_base, Session
from datetime import datetime
from typing import Optional

#Configurar url do SQL lite BASE
DATABASE_URL = "sqlite:///./eventos.db"
engine = create_engine(DATABASE_URL, echo=False, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit= False, autoflush= False, bind=engine)
Base = declarative_base()

#Criar modelo ORM
class Evento(Base):
    __tablename__ = 'eventos'
    id = Column(Integer, primary_key= True)
    nome = Column(String(255), nullable= False)
    data_hora = Column(DateTime, nullable= False)

#Criar tudo no banco de dados
Base.metadata.create_all(bind=engine)

#Função de fechar sessão
def get_db():
    db = SessionLocal()
    try:
        yield db #Comando de contexto do banco de dados
    finally:
        db.close()

#Modelos Pydantic
class EventoBase(BaseModel): #Dicionário de dados
    nome: str
    data_hora: datetime

class EventoCreate(EventoBase):
    pass

class EventoUpdate(BaseModel): #Validar tipo da informação quando houver atualização
    nome: Optional[str] = None
    data_hora: Optional[datetime] = None

class EventoResponse(EventoBase): #Atribuir id
    id: int

    class Config: #Configurar para se comunicar com o ORM
        from_attributes = True

#CRUD
def criar_evento(db: Session, evento: EventoCreate): #Salvar no BD
    db_evento = Evento(nome=evento.nome, data_hora=evento.data_hora)
    db.add(db_evento)
    db.commit()
    db.refresh(db_evento)
    return db_evento

def listar_eventos(db: Session):
    return db.query(Evento).all()

def obter_evento(db: Session, evento_id: int):
    return db.query(Evento).filter(Evento.id == evento_id).first()

def atualizar_evento(db: Session, evento_id: int, evento: EventoUpdate):
    db_evento = obter_evento(db, evento_id)
    if not db_evento:
        return None
    if evento.nome:
        db_evento.nome = evento.nome
    if evento.data_hora:
        db_evento.data_hora = evento.data_hora
    db.commit()
    db.refresh(db_evento)
    return db_evento

def deletar_evento(db: Session, evento_id: int):
    db_evento = obter_evento(db, evento_id)
    if not db_evento:
        return False
    db.delete(db_evento)
    db.commit()
    return True

#Construção da API
app = FastAPI(title='Gerenciador de Eventos API', version='1.0.0')

#Comunicar front com back
app.add_middleware( 
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

#Endpoints da Api
@app.get('/')
def root():
    return {'mensagem': 'Bem-vindo ao Gerenciador de Eventos API'}

@app.post('/eventos/', response_model=EventoResponse, status_code=201)
def criar_novo_evento(evento: EventoCreate, db: Session = Depends(get_db)):
    return criar_evento(db, evento)

@app.get('/eventos/', response_model = list[EventoResponse])
def listar_todos_eventos(db: Session = Depends(get_db)):
    return listar_eventos(db)

@app.get('/eventos/{evento_id}', response_model=EventoResponse)
def obter_evento_por_id(evento_id: int, db: Session = Depends(get_db)):
    evento = obter_evento(db, evento_id)
    if not evento:
        raise HTTPException(status_code=404, detail='Evento não encontrado')
    return evento

@app.put('/eventos/{evento_id}', response_model=EventoResponse)
def atualizar_evento_por_id(evento_id: int, evento: EventoUpdate, db: Session = Depends(get_db)):
    evento_atualizado = atualizar_evento(db, evento_id, evento)
    if not evento_atualizado:
        raise HTTPException(status_code=404, detail='Evento não encontrado')
    return evento_atualizado

@app.delete('/eventos/{evento_id}', status_code=204)
def deletar_evento_por_id(evento_id: int, db: Session = Depends(get_db)):
    if not deletar_evento(db, evento_id):
        raise HTTPException(status_code=404, detail='Evento não encontrado')
    return None