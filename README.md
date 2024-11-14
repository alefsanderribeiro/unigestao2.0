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
- [Cadastro de Funcionários e Vínculo Empregatício](#cadastro-de-funcionários)
- [Ferramentas utilizadas](#ferramentas-utilizadas)
- [Acesso ao projeto](#acesso-ao-projeto)
- [Abrir e rodar o projeto](#abrir-e-rodar-o-projeto)
- [Acesso Inicial e Recomendações de Segurança](#acesso-inicial-e-recomendações-de-segurança)
- [Próximas Etapas](#próximas-etapas)
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

### Dashboard

![Formulário de Cadastro de Funcionários Dados Pessoais](https://github.com/MarcosSerra1/unigestao2.0/blob/main/static/image/imagens_sistema/dashboard.png)

### Formulário de Cadastro de Funcionários

![Formulário de Cadastro de Funcionários Dados Pessoais](https://github.com/MarcosSerra1/unigestao2.0/blob/main/static/image/imagens_sistema/cadastro_funcionarios_01.png)

![Formulário de Cadastro de Funcionários Naturalidade](https://github.com/MarcosSerra1/unigestao2.0/blob/main/static/image/imagens_sistema/cadastro_funcionarios_02.png)

![Formulário de Cadastro de Funcionários Documentos](https://github.com/MarcosSerra1/unigestao2.0/blob/main/static/image/imagens_sistema/cadastro_funcionarios_03.png)

![Formulário de Cadastro de Funcionários Carteira de Trabalho](https://github.com/MarcosSerra1/unigestao2.0/blob/main/static/image/imagens_sistema/cadastro_funcionarios_04.png)

![Formulário de Cadastro de Funcionários Naturalidade Dados Complementares](https://github.com/MarcosSerra1/unigestao2.0/blob/main/static/image/imagens_sistema/cadastro_funcionarios_05.png)

![Formulário de Cadastro de Funcionários Contato](https://github.com/MarcosSerra1/unigestao2.0/blob/main/static/image/imagens_sistema/cadastro_funcionarios_06.png)

### Exemplo de Funcionário Cadastrado

![Funcionário Cadastrado](https://github.com/MarcosSerra1/unigestao2.0/blob/main/static/image/imagens_sistema/listagem_funcionarios.png)

### Formulário Para Cadastrar Vínculo Empregatício

![Funcionário Cadastrado](https://github.com/MarcosSerra1/unigestao2.0/blob/main/static/image/imagens_sistema/vinculo.png)

### Exemplo de Vínculo Empregatício

![Funcionário Cadastrado](https://github.com/MarcosSerra1/unigestao2.0/blob/main/static/image/imagens_sistema/listagem_vinculos.png)

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

8. População de Dados Cadastrais e Vínculo Empregatício:
   
    População para Gênero, Raça, Estado Civil, Deficiência, Grau de Instrução e Nacionalidade:

      ```
      python manage.py loaddata configurations/fixtures/*.json
      ```

9. População de Dados CBOs:

    População para CBOs, Ocupação e Sinônimos:

     ```
     python manage.py loaddata cbos/fixtures/*.json
     ```

10. População de Dados Geográficos:

    População para Países, Estados, Capitais, Cidades e Região:

     ```
     python manage.py loaddata geography/fixtures/*.json
     ```

11. Inicie o servidor:

    ```
    python manage.py runserver
    ```

12. Acesse a aplicação em seu navegador em [http://localhost:8000](http://localhost:8000).

## Acesso Inicial e Recomendações de Segurança

Assim que o sistema estiver rodando, **é necessário acessar com um superusuário** para configurar o sistema. Para evitar que usuários regulares possam apagar dados sensíveis ou realizar alterações indevidas, recomenda-se a criação de grupos com permissões específicas.

### Recomendações de Grupos de Usuários

- **Usuário de Nível 1**: Este grupo terá acesso apenas aos apps `employees` e `bond`, que são responsáveis pelo gerenciamento de funcionários e vínculos. Usuários desse grupo podem visualizar e acessar esses dados sem riscos de interferir em outras configurações do sistema.

Esta organização ajuda a proteger os dados, garantindo que o sistema seja utilizado de forma mais segura e eficiente, especialmente em ambientes com múltiplos usuários.

## Próximas Etapas

Abaixo estão os recursos e melhorias planejados para a próxima fase de desenvolvimento do Uni Gestão:

- **Gerenciamento de Pagamentos**: Criação de um app para controlar pagamentos, com funcionalidades para identificar se estão feitos, atrasados, ou adiantados, visando melhor controle financeiro.

- **Geração Automática de Contratos**: Desenvolvimento de uma ferramenta para criar contratos personalizados, que serão armazenados e gerenciados diretamente no sistema, automatizando processos e evitando trabalho manual repetitivo.

Essas etapas serão implementadas progressivamente para aprimorar a funcionalidade e a experiência do usuário.

## Desenvolvedores

| [<img loading="lazy" src="https://avatars.githubusercontent.com/u/78652932?v=4" width=115><br><sub>Marcos Serra</sub>](https://github.com/MarcosSerra1) |
| :---: |
| **Marcos Serra** - Desenvolvedor principal do projeto, responsável pela arquitetura e desenvolvimento das funcionalidades principais. |
