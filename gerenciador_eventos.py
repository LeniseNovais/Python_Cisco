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
            print('❌ Erro ao carregar eventos. Iniciando com uma lista vazia')
            return []
    else:
        return []
    
def salvar_eventos(caminho_arquivo, eventos):
    try:
        with open(caminho_arquivo, 'w', encoding='utf-8') as arquivo:
            json.dump(eventos, arquivo,  indent=2, ensure_ascii=False)
        print('Evento salvo ☑️')
    except IOError as e:
        print(f'⚠️ Erro ao salvar os eventos; {e}')

def adicionar_evento(eventos, caminho_arquivo):
    titulo = input('Digite o título do evento: ').strip()
    if not titulo:
        print('⚠️ O título do evento não pode ficar vazio')
        return
    data_hora_valida = False
    data_hora_str = None

    while not data_hora_valida:
        try:
            data_hora_str = input('Digite a data e a hora do evento (formato: DD/MM/AAA HH:MM): ').strip()
            datetime_obj = datetime.strptime(data_hora_str, '%d/%m/%Y %H:%M')
            data_hora_valida = True
            data_hora_str = datetime_obj.isoformat()
        except ValueError:
            print('⚠️ Formato de data e hora inválido. Por favor, tente novamente.')


    evento = {
            'titulo': titulo,
            'data_hora': data_hora_str
    }
    eventos.append(evento)

    #Salva eventos no arquivo
    salvar_eventos(caminho_arquivo, eventos)
    print(f"'{titulo}' adicionado com sucesso ✅")
  
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
        print(f"{i}. {evento['titulo']} - {data_formatada} {status}")
        print('-' * 40)

def visualizar_calendario():
    '''
    Exibe o calendário de um mês específico
    Args:
        None
    Retorna:
        None
    '''
    print('\n' + '=' * 50)
    print('📆  VISUALIZAR CALENDÁRIO  📆')
    print('=' * 50)

    try:
        #Solicita ano
        ano = int(input('\n Ano (ex: AAAA): '))

        #Solicita mês
        mes = int(input('\n Mês (ex: MM): '))

        #Validação simples do mês
        if mes < 1 or mes > 12:
            print('❌ O MÊS deve estar entre 01 e 12. \n')
            return

        #Obtém os nomes do mês em português
        nomes_meses = [
            "","Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
            "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"            
        ]

        print(f'\n 🗓️  Calendário de {nomes_meses[mes]} de {ano}\n')

        #Função para exibir calendários de forma organizada
        calendario = calendar.month(ano, mes)
        print(calendario)
    
    except ValueError:
        print('❌ Entrada inválida! Use números inteiros para ano e mês \n')

def menu_principal():
    '''
    Menu principal do programa
    Args:
        None
    Retorna:
        None
    '''
    #Configura o ambiente (cria pastas e define caminhos)
    caminho_arquivo = configurar_ambiente()

    #Carrega os eventos existentes
    eventos = carregar_eventos(caminho_arquivo)

    #Loop principal programa
    #Continua até usuário selecionar SAIR
    while True:
        print('\n' + '='*50)
        print('           🗓️  GERENCIADOR DE EVENTOS')
        print('='* 50)
        print('\n  1️⃣  Adicionar evento')
        print('  2️⃣  Listar eventos')
        print('  3️⃣  Visualizar calendário')
        print('  4️⃣  SAIR')
        print('\n' + '='*50)

        #Solicita opção
        opcao = input('\n  ✅ Escolha uma opção (1-4): ').strip()

        #Estrutura para tratar cada opção
        if opcao == '1':
            adicionar_evento(eventos, caminho_arquivo)
            #Recarregar os eventos após adicionar
            eventos = carregar_eventos(caminho_arquivo)
        
        elif opcao == '2':
            listar_eventos(eventos)
        
        elif opcao == '3':
            visualizar_calendario()
        
        elif opcao == '4':
            print('\n Até logo! 👋🏻 Programa encerrado. \n')
            break

        else:
            #Opção inválida
            print('❌ Opção inválida! Por favor, escolha as opções de 1 a 4 \n')
    
if __name__ == '__main__':
    menu_principal()