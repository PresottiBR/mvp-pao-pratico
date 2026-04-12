#  LogControl - Backend API

API desenvolvida para o sistema **LogControl**, um MVP de controle logístico de carregamentos.

##  Objetivo

A API tem como finalidade registrar e gerenciar informações de carregamentos, garantindo organização, rastreabilidade e evitando divergências nos dados logísticos.

---

##  Tecnologias utilizadas

* Python
* Flask
* SQLite
* Flasgger (Swagger)
* Flask-CORS

---

## Funcionalidades

A API permite:

* ✔ Cadastrar carregamentos
* ✔ Listar todos os carregamentos
* ✔ Buscar carregamento por ID
* ✔ Deletar carregamento

---

##  Rotas da API

###  Criar carregamento

`POST /carregamento`

###  Listar carregamentos

`GET /carregamentos`

###  Buscar por ID

`GET /carregamento/{id}`

###  Deletar carregamento

`DELETE /carregamento/{id}`

---

##  Documentação (Swagger)

A documentação interativa da API pode ser acessada em:

http://127.0.0.1:5000/apidocs

---

##  Como executar o projeto

### 1. Acesse a pasta do backend

```bash
cd backend-api
```

### 2. Ative o ambiente virtual

```bash
source ../.venv/bin/activate
```

### 3. Instale as dependências (se necessário)

```bash
pip install flask flask-cors flasgger
```

### 4. Execute a aplicação

```bash
python app.py
```

---

##  Endpoints principais

* API base: http://127.0.0.1:5000
* Swagger: http://127.0.0.1:5000/apidocs
* Listagem: http://127.0.0.1:5000/carregamentos

---

##  Observações

* O banco de dados SQLite é criado automaticamente ao iniciar a aplicação.
* Os dados são armazenados localmente no arquivo `database.db`.
* Este projeto foi desenvolvido como MVP, podendo ser expandido com autenticação e validações mais avançadas.

---

##  Autor

Tiago Presotti Borges
