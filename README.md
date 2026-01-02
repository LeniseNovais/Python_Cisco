# 🗓️ Gerenciador de Eventos Full-Stack em Python

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green?logo=fastapi)
![Streamlit](https://img.shields.io/badge/Streamlit-Frontend-red?logo=streamlit)
![SQLite](https://img.shields.io/badge/SQLite-Database-lightgrey)
![Status](https://img.shields.io/badge/Status-Em%20Evolução-yellow)

Um **gerenciador de eventos completo**, com backend em **FastAPI**, banco de dados **SQLite** e frontend em **Streamlit**.  
Aqui a ideia foi sair do script simples e evoluir para algo mais próximo do mundo real: **API, persistência, front separado e comunicação via HTTP**.

Tudo feito com Python, do começo ao fim.

---

## ✨ Visão geral do projeto

Esse projeto permite **criar, listar, editar, excluir e importar eventos**, além de visualizar tudo em formato de lista ou calendário mensal.

Ele nasceu no terminal e foi crescendo, ganhando:
- API REST
- banco de dados relacional
- interface visual
- separação clara entre responsabilidades

---

## 🧠 Arquitetura

O projeto segue uma separação simples e funcional:

- **Backend** → FastAPI + SQLAlchemy + SQLite  
- **Frontend** → Streamlit consumindo a API  
- **Comunicação** → HTTP (REST)  
- **Persistência** → Banco de dados local  

---

## 🚀 Funcionalidades

✔️ Criar eventos com nome, data e hora  
✔️ Listar eventos ordenados cronologicamente  
✔️ Identificar eventos passados e futuros  
✔️ Editar eventos existentes  
✔️ Deletar eventos  
✔️ Visualizar eventos em calendário mensal  
✔️ Filtrar eventos (todos, semana, mês)  
✔️ Importar eventos a partir de arquivo `.json`  
✔️ Persistência real em banco de dados SQLite  

---

## 🧩 Tecnologias e conceitos utilizados

- **Python**
- **FastAPI**
- **Streamlit**
- **SQLAlchemy (ORM)**
- **SQLite**
- **Pydantic (validação de dados)**
- **CRUD completo**
- **API REST**
- **CORS**
- **Datetime e Calendar**
- **Requests (consumo da API)**
- **Ambiente virtual (venv)**

---

## 📂 Estrutura do projeto

```bash
PythonCisco/
│
├── backend/
│   ├── main.py          # API FastAPI
│   └── eventos.db       # Banco SQLite
│
├── frontend/
│   └── app.py           # Interface Streamlit
│
├── dados/
│   └── eventos.json     # Arquivo para importação
│
├── .venv/
│
└── README.md
```

---

## ▶️ Como executar o projeto

### 1️⃣ Clonar o repositório

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```

### 2️⃣ Ativar o ambiente virtual (Windows)
```bash
.\.venv\Scripts\Activate.ps1
```
- Caso a execução de scripts esteja bloqueada no Windows:
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

### 3️⃣ Iniciar o backend (FastAPI)
```bash
uvicorn backend.main:app --reload
```
- A API ficará disponível em:
http://127.0.0.1:8000

- A documentação automática (Swagger) pode ser acessada em:
http://127.0.0.1:8000/docs

### 4️⃣ Iniciar o frontend (Streamlit)
```bash
streamlit run frontend/app.py
```
A interface será aberta automaticamente no navegador 🚀

## 📡 Endpoints da API
| Método | Endpoint        | Descrição               |
| ------ | --------------- | ----------------------- |
| GET    | `/`             | Mensagem de boas-vindas |
| POST   | `/eventos/`     | Criar evento            |
| GET    | `/eventos/`     | Listar eventos          |
| GET    | `/eventos/{id}` | Buscar evento por ID    |
| PUT    | `/eventos/{id}` | Atualizar evento        |
| DELETE | `/eventos/{id}` | Deletar evento          |

Todos os endpoints possuem validação com Pydantic e persistência via SQLAlchemy + SQLite.

## 📩 Importação de eventos
O frontend permite importar eventos por meio de um arquivo .json, realizando:

- leitura do arquivo

- validação dos dados

- conversão de datas

- envio automático para a API

Ao final, o sistema informa:

- quantidade de eventos importados

- quantidade de erros

- detalhes dos erros encontrados
