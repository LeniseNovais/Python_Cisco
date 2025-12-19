import os
import json
from datetime import datetime
import time
import calendar

def configurar_ambiente():
    """ Configurar o ambiente de trabalho para o gerenciador de evento"""
    pasta_dados = "dados"
    os.makedirs(pasta_dados, exist_ok=True)
    caminho_arquivo = os.path.join(pasta_dados, "evento.json")

    return caminho_arquivo

def carregar_eventos(caminho_arquivo):
    if os.path.exists(caminho_arquivo):
        try:
            with open(caminho_arquivo, 'r') as arquivo:
                eventos = json.load(arquivo)
                return eventos
        except (json.JSONDecodeError, IOError):
            print('Erro ao carregar eventos. Iniciando com uma lista vazia')
            return []
    else:
        return []
    
def salvar_eventos(caminho_arquivo, eventos):
    try:
        with open(caminho_arquivo, 'w', encoding='utf-8') as arquivo:
            json.dump(eventos, arquivo,  indent=2, ensure_ascii=False)
        print('Eventos salvos com sucesso')
    except IOError as e:
        print(f'Erro ao salvar os eventos; {e}')

def adicionar_evento(eventos):
    titulo = input('Digite o título do evento: ').strip()
    if not titulo:
        print('O título do evento não pode ficar vazio')
        return
    data_hora_valida = False
    data_hora_str = None

    while not data_hora_valida:
        try:
            data_hora_str = input('Digite a data e a hora do evento (formato: DD-MM-AAA HH:MM): ').strip()
            datetime_obj = datetime.strptime(data_hora_str, '%d/%m/%Y %H:%M')
            data_hora_valida = True
            data_hora_str = datetime_obj.isoformat()
        except ValueError:
            print('Formato de data e hora inválido. Por favor, tente novamente.')


    evento = {
            'titulo': titulo,
            'data_hora': data_hora_str
    }
    eventos.append(evento)
    print(f'Evento' {titulo} 'adicionado com sucesso')
  
def listar_eventos(eventos):
    if not eventos:
        print('Nenhum evento cadastrado.')
        return
    eventos_ordenados = sorted(eventos, key=lambda e: e['data_hora'])
    agora = datetime.now()

    print('\n Eventos cadastrados: \n')

    for i, evento in enumerate(eventos_ordenados, start=1):
        data_hora_obj = datetime.fromisoformat(evento['data_hora'])

        if data_hora_obj < agora:
            status = '[Passado]'
        else:
            status = "[Futuro]"
        
        data_formatada = data_hora_obj.strftime('%d/%m/%Y %H:%M')
        print(f'{i}. {evento['título']} - {data_formatada} {status}')
        print('-' *40)