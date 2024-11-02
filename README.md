<div align="center">
  <img src="https://github.com/MarcosSerra1/unigestao2.0/blob/main/static/image/Design%20sem%20nome.png" alt="Logo Uni Gestão" width="200" height="200"/>
</div>

# Uni Gestão

<div align="center">
  
  ![Badge Licença](https://badgen.net/static/license/MIT/green)  ![Badge em Desenvolvimento](https://badgen.net/static/status/EM%20DESENVOLVIMENTO/green)
  
</div>

### Tópicos 

- [Descrição do projeto](#descrição-do-projeto)

- [Funcionalidades](#funcionalidades)

- [Ferramentas utilizadas](#ferramentas-utilizadas)

- [Acesso ao projeto](#acesso-ao-projeto)

- [Abrir e rodar o projeto](#abrir-e-rodar-o-projeto)

- [Desenvolvedores](#desenvolvedores)

## Descrição do projeto

<p align="justify">
  Este projeto é um sistema web desenvolvido em Django, com o objetivo de gerenciar informações de funcionários, fornecedores e clientes de maneira eficiente e organizada. A aplicação permite o cadastro, edição e visualização de dados, além da emissão de notas fiscais.
</p>

## Funcionalidades

- **Cadastro de Funcionários**: Registro de informações pessoais, documentos e dados complementares, com referência a cargos e vínculos em tabelas futuras.
- **Gerenciamento de Fornecedores**: Controle de dados de fornecedores, facilitando a comunicação e o rastreamento de serviços.
- **Cadastro de Clientes**: Registro detalhado de informações sobre clientes, permitindo um melhor acompanhamento e relacionamento.
- **Emissão de Notas Fiscais**: Integração com uma API para gerar notas fiscais de forma prática e automatizada.
- **Interface Responsiva**: Uso do Bootstrap 5 para garantir uma interface de usuário moderna e responsiva, com um layout dinâmico e funcional.

## Ferramentas utilizadas

- Django como framework principal para desenvolvimento web.
- Bootstrap 5 para estilização e design responsivo.
- Python como linguagem de programação.
- Banco de dados PostgreSQL para armazenamento eficiente de informações.

## Acesso ao projeto

Você pode [acessar o código fonte do projeto](https://github.com/MarcosSerra1/unigestao2.0) ou [baixá-lo](https://github.com/MarcosSerra1/unigestao2.0/archive/refs/heads/main.zip).

## Abrir e rodar o projeto

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

8. Inicie o servidor:

    ```
    python manage.py runserver
    ```

9. Acesse a aplicação em seu navegador em http://localhost:8000.

## Desenvolvedores

| [<img loading="lazy" src="https://avatars.githubusercontent.com/u/78652932?v=4" width=115><br><sub>Marcos Serra</sub>](https://github.com/MarcosSerra1) |
| :---: |
