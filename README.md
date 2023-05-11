<h1 align="center">API REST - Find it - Django Ninja</h1>

Criação de API Rest usando Django Ninja.

## 🛠️ Ferramentas e Tecnologias

- Python 
- Django 
- Django Ninja
- IDE: Pycharm
- SQLite 

## ⚙ Funcionalidades

- Criar tarefa
- Cadastrar tarefa
- Deletar tarefa
- Atualizar tarefa

## 💻 Como executar o projeto

Antes de iniciar a aplicação é necessário a instalação das seguintes ferramentas: Python, Git e IDE de sua preferência. 
É recomendado a criação ambiente venv antes de instalar os requirements.txt

- Clone esse repositório:

  ```$ git clone <https://github.com/ViniciusRaony/api-django-findit.git>```

- Instale as dependências:

  ```$ pip install -r requirements.txt```

- Execute a aplicação:
 
  ```$ python manage.py runserver```

- URL para acessar servidor local:

  ```acesse http://localhost:8000/``` 


## 🚉 Rotas da API


- Rota ```/v1/api/docs``` Swagger

- Rota ```/v1/api/cadastro``` (método ```POST```): Cadastrar tarefa

-  Rota ```/v1/api/cadastro``` (método ```GET```): Retorna todas as tarefas

- Rota ```/v1/api/cadastro/id``` (método ```GET```): Retornar tarefa por ID

- Rota ```/v1/api/cadastro/id``` (método ```PUT```): Atualizar tarefa

- Rota ```/v1/api/cadastro/id``` (método ```DELETE```): Deletar tarefa


### Links úteis

- [Documentação Django Ninja: [https://django-ninja.rest-framework.com/](https://django-ninja.rest-framework.com/)


### Pré-requisitos

Antes de começar, você vai precisar ter instalado em sua máquina as seguintes ferramentas:
[Git](https://git-scm.com)

É bom ter um editor para trabalhar com o código como [VSCode](https://code.visualstudio.com/).

Ter instalado [Python](https://www.python.org/) na sua máquina.

