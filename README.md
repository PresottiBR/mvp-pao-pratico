# LogControl – Sistema de Controle Logístico

O **LogControl** é um sistema web desenvolvido como **MVP (Minimum Viable Product)** para controle logístico de carregamentos.

O objetivo do projeto é registrar e acompanhar informações de transporte de forma organizada e precisa, garantindo maior transparência no processo logístico.

O sistema foi criado para evitar divergências de informações e possíveis irregularidades, garantindo que todos os dados de carregamento fiquem registrados corretamente. Dessa forma, caso haja descumprimento de ordens, inconsistências ou suspeitas de furtos, as informações registradas permitem identificar facilmente o que ocorreu.

---

## Funcionalidades

* Registro de carregamentos
* Cadastro de motorista
* Registro de veículo
* Registro de placa
* Armazenamento em banco de dados
* Listagem de carregamentos registrados
* API documentada com Swagger

---

## Tecnologias Utilizadas

### Backend

* Python
* Flask
* SQLite
* Flasgger (Swagger)

### Frontend

* HTML
* CSS
* JavaScript

---

## Estrutura do Projeto

logcontrol
│
├── backend-api
│   ├── app.py
│   └── database.db
│
├── frontend-app
│   └── index.html
│
└── README.md

---

## Como Executar o Projeto

### 1 Clonar o repositório

git clone https://github.com/PresottiBR/LogControl-MVP

### 2 Acessar a pasta do backend

cd backend-api

### 3 Ativar ambiente virtual

source ../.venv/bin/activate

### 4 Executar a API

python3 app.py

A API será executada em:

http://127.0.0.1:5000

---

## Documentação da API (Swagger)

A documentação da API pode ser acessada em:

http://127.0.0.1:5000/apidocs

---

## Interface do Sistema

O frontend foi desenvolvido em **HTML, CSS e JavaScript**, permitindo registrar carregamentos e visualizar os dados registrados.

Após iniciar a API, a interface pode ser acessada em:

http://127.0.0.1:5000/app

### Exemplo da Interface

![LogControl](images/logcontrol.png)
---

## Autor

**Tiago Presotti Borges**

