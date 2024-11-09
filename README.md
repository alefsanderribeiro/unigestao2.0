<div align="center">
  <img src="https://github.com/MarcosSerra1/unigestao2.0/blob/main/static/image/logo/logo_unigestao.png" alt="Logo Uni Gestão" width="200" height="200"/>
</div>

# Uni Gestão

<div align="center">
  
  ![Badge Licença](https://badgen.net/static/license/MIT/green)  ![Badge em Desenvolvimento](https://badgen.net/static/status/EM%20DESENVOLVIMENTO/yellow)
  
</div>

### Tópicos 

- [Descrição do projeto](#descrição-do-projeto)
- [Funcionalidades](#funcionalidades)
- [Cadastro de Funcionários (com as imagens)](#cadastro-de-funcionários)
- [Ferramentas utilizadas](#ferramentas-utilizadas)
- [Acesso ao projeto](#acesso-ao-projeto)
- [Abrir e rodar o projeto](#abrir-e-rodar-o-projeto)
- [Desenvolvedores](#desenvolvedores)

## Descrição do projeto

Este é o **Uni Gestão**, um sistema web desenvolvido com Django para gerenciar de forma eficiente e segura as informações de funcionários, fornecedores e clientes. O sistema facilita o cadastro, a edição e a visualização de dados essenciais, além de integrar funcionalidades como emissão automatizada de notas fiscais. Ideal para empresas que buscam organizar seu fluxo de trabalho e otimizar processos.


## Funcionalidades

- **Cadastro de Funcionários**: Registre informações detalhadas dos funcionários, como dados pessoais, documentos e referências a cargos. Possui integração com tabelas de vínculos e cargos que serão expandidas futuramente.
- **Gerenciamento de Fornecedores**: Controle os dados dos fornecedores, incluindo contatos, serviços prestados e outros detalhes que facilitam o gerenciamento e acompanhamento das relações.
- **Cadastro de Clientes**: Adicione informações detalhadas dos clientes, permitindo um controle mais eficiente sobre as interações e necessidades dos mesmos.
- **Emissão de Notas Fiscais**: Automatize a geração de notas fiscais utilizando uma integração com uma API externa para garantir um processo ágil e sem erros.
- **Interface Responsiva**: Uso do Bootstrap 5 para garantir uma interface de usuário moderna e responsiva, com um layout dinâmico e funcional.

## Cadastro de Funcionários

Aqui estão algumas imagens que ilustram o processo de cadastro de funcionários na aplicação.

### Formulário de Cadastro

![Formulário de Cadastro de Funcionários](https://github.com/MarcosSerra1/unigestao2.0/blob/main/static/image/employees/formulario_1.png)

![Formulário de Cadastro de Funcionários](https://github.com/MarcosSerra1/unigestao2.0/blob/main/static/image/employees/formulario_2.png)

### Exemplo de Funcionário Cadastrado

![Funcionário Cadastrado](https://github.com/MarcosSerra1/unigestao2.0/blob/main/static/image/employees/tela_listagem.png)


## Ferramentas utilizadas

- **Django**: Framework principal para desenvolvimento web.
- **Bootstrap 5**: Framework CSS para estilização e design responsivo.
- **Python**: Linguagem de programação principal.
- **PostgreSQL**: Banco de dados para armazenamento eficiente de informações.

## Acesso ao projeto

Você pode [acessar o código fonte do projeto](https://github.com/MarcosSerra1/unigestao2.0) ou [baixá-lo](https://github.com/MarcosSerra1/unigestao2.0/archive/refs/heads/main.zip).

## Abrir e rodar o projeto

### Versões recomendadas

- Python 3.x
- Django 4.x

### Passos para rodar o projeto localmente:

#### Observação sobre Banco de Dados

O projeto é configurado para usar o **PostgreSQL** quando rodando dentro de containers Docker e o **SQLite** quando rodando sem Docker. Você pode alternar entre esses dois bancos de dados alterando o valor da variável `DOCKER_MODE` nas configurações do Django.

- **Com Docker (PostgreSQL)**: Quando o Docker está em uso, o banco de dados utilizado é o PostgreSQL. Para garantir a conexão correta, a variável `DOCKER_MODE` deve ser configurada como `True`. O arquivo `.env` deve conter as configurações do banco de dados, como nome, usuário e senha.
  
- **Sem Docker (SQLite)**: Caso você não queira usar o Docker, basta configurar `DOCKER_MODE` como `False`. Nesse caso, o projeto usará o banco de dados SQLite, que é mais simples de configurar e pode ser usado para testes rápidos ou em ambientes de desenvolvimento.

No arquivo de configurações `settings.py`, o comportamento é controlado pela seguinte variável:

```python
DOCKER_MODE = True  # Altere para False para usar SQLite

if DOCKER_MODE:
    load_dotenv()
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.getenv('DB_NAME'),
            'USER': os.getenv('DB_USER'),
            'PASSWORD': os.getenv('DB_PASSWORD'),
            'HOST': os.getenv('DB_HOST'),
            'PORT': os.getenv('DB_PORT'),
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
```

Se você optar por usar o PostgreSQL com Docker, basta definir as variáveis de ambiente no arquivo `.env`.

#### Usando Docker

1. Certifique-se de ter o Docker e o Docker Compose instalados. Você pode baixar o Docker em https://www.docker.com/get-started.
   
2. Clone este repositório para o seu ambiente local.

3. Navegue até o diretório do projeto no terminal.

4. Crie um arquivo `.env` com as variáveis de ambiente necessárias para a conexão do banco de dados e superusuário:

    ```
    # BD Conexão
    DB_NAME=name-bd
    DB_USER=user-bd
    DB_PASSWORD=password-bd
    DB_HOST=db
    DB_PORT=5432

    # SuperUser Django
    DJANGO_SUPERUSER_USERNAME=super-user
    DJANGO_SUPERUSER_PASSWORD=password-user
    DJANGO_SUPERUSER_EMAIL=superuser@exemplo.com

    ```

5. Rode os containers com o comando:

    ```
    docker-compose up --build
    ```

6. O Docker irá construir a imagem, configurar o banco de dados e rodar o servidor Django. Você pode acessar a aplicação em seu navegador em [http://localhost:8000](http://localhost:8000).

7. Para rodar a aplicação sem o Docker, siga as etapas abaixo.

#### Sem Docker

1. Certifique-se de ter o Python instalado. Você pode baixá-lo em https://www.python.org/.
2. Clone este repositório para o seu ambiente local.
3. Navegue até o diretório do projeto no terminal.
4. Crie um ambiente virtual:

    ```
    python -m venv venv
    ```

5. Ative o ambiente virtual:

    - No Windows:

    ```
    venv\Scripts\activate
    ```

    - No macOS e Linux:

    ```
    source venv/bin/activate
    ```

6. Instale as dependências do projeto:

    ```
    pip install -r requirements.txt
    ```

7. Execute as migrações do Django para criar o banco de dados:

    ```
    python manage.py migrate
    ```

8. População de Dados Cadastrais:
   
    População para Gênero, Raça, Estado Civil, Deficiência, Grau de Instrução e Nacionalidade:

      ```
      python manage.py loaddata employees/fixtures/gender.json
      python manage.py loaddata employees/fixtures/race.json
      python manage.py loaddata employees/fixtures/maritalstatus.json
      python manage.py loaddata employees/fixtures/deficiency.json
      python manage.py loaddata employees/fixtures/degreeinstruction.json
      python manage.py loaddata employees/fixtures/nationality.json
      ```

10. População de Dados Geográficos:

    População para Países, Estados, Capitais, Cidades e Região:

     ```
     python manage.py loaddata geography/fixtures/0_pais.json
     python manage.py loaddata geography/fixtures/1_estados.json
     python manage.py loaddata geography/fixtures/2_capitais.json
     python manage.py loaddata geography/fixtures/3_cidades.json
     python manage.py loaddata geography/fixtures/4_regiao.json
     ```


10. Inicie o servidor:

    ```
    python manage.py runserver
    ```

11. Acesse a aplicação em seu navegador em [http://localhost:8000](http://localhost:8000).

## Desenvolvedores

| [<img loading="lazy" src="https://avatars.githubusercontent.com/u/78652932?v=4" width=115><br><sub>Marcos Serra</sub>](https://github.com/MarcosSerra1) |
| :---: |
| **Marcos Serra** - Desenvolvedor principal do projeto, responsável pela arquitetura e desenvolvimento das funcionalidades principais. |
