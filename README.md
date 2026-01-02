# 🗓️ Gerenciador de Eventos em Python

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Status](https://img.shields.io/badge/Status-Concluído-yellow)
![Terminal](https://img.shields.io/badge/Interface-Terminal-lightgrey)

Um **gerenciador de eventos via terminal**, criado em Python, com foco em organização, simplicidade e aprendizado prático.  
A ideia aqui é transformar conceitos da linguagem em algo útil no dia a dia — sem interface gráfica, sem mágica, só código bem estruturado.

---

## ✨ Sobre o projeto

Esse projeto permite **criar, listar e visualizar eventos**, salvando tudo em arquivo `.json`, de forma persistente.  
Ele foi pensado como um exercício prático para treinar:

- lógica de programação  
- organização de código em funções  
- leitura e escrita de arquivos  
- tratamento de erros  
- interação com usuário via terminal  

Tudo isso mantendo um código limpo, legível e fácil de evoluir.

---

## 🚀 Funcionalidades

✔️ Adicionar eventos com título, data e hora  
✔️ Listar eventos cadastrados (ordenados por data)  
✔️ Identificar eventos **passados** e **futuros**  
✔️ Visualizar calendário mensal diretamente no terminal  
✔️ Persistência dos dados em arquivo JSON  
✔️ Menu interativo simples e intuitivo  

---

## 🧠 Tecnologias e conceitos utilizados

- **Python**
- Manipulação de arquivos (`json`)
- Datas e horários (`datetime`)
- Calendário (`calendar`)
- Estruturas de repetição e decisão
- Boas práticas com funções
- Ambiente virtual (`venv`)

---

## 📂 Estrutura do projeto

```bash
PythonCisco/
│
├── dados/
│   └── evento.json
│
├── .venv/
│
├── gerenciador_eventos.py
│
└── README.md
