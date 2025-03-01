<div align="center">
  <img src="https://github.com/MarcosSerra1/unigestao2.0/blob/main/static/image/logo/logo_unigestao.png" alt="Logo Uni Gestão" width="200" height="200"/>
  
# **Uni Gestão**
  
  Gerencie informações de funcionários, fornecedores e clientes de forma eficiente e segura.
  
  ![Badge Licença](https://badgen.net/static/license/MIT/green)  ![Badge em Desenvolvimento](https://badgen.net/static/status/EM%20DESENVOLVIMENTO/black) ![Badge Versão](https://badgen.net/static/version/2.0.3/orange)
</div>

## Tópicos

- [Descrição do Projeto](#descrição-do-projeto)
- [Principais Funcionalidades](#principais-funcionalidades)
- [Detalhes do Cadastro de Funcionários e Vínculos Empregatícios](#detalhes-do-cadastro-de-funcionários-e-vínculos-empregatícios)
- [Ferramentas Utilizadas](#ferramentas-utilizadas)
- [Como Acessar o Projeto](#como-acessar-o-projeto)
- [Instruções para Rodar o Projeto](#instruções-para-rodar-o-projeto)
- [Acesso Inicial e Segurança](#acesso-inicial-e-segurança)
- [Próximas Funcionalidades](#próximas-funcionalidades)
- [Sobre o Desenvolvedor](#sobre-o-desenvolvedor)

## Descrição do Projeto

O **Uni Gestão** é um sistema web desenvolvido com Django para empresas que buscam:

- Organização centralizada de dados de funcionários, fornecedores e clientes.
- Integração com APIs externas para automação, como a emissão de notas fiscais.
- Agilidade e segurança no gerenciamento de dados essenciais.

Este sistema é ideal para otimizar processos internos, reduzindo erros e promovendo eficiência no fluxo de trabalho empresarial.

## Principais Funcionalidades

- **Cadastro de Funcionários**: Registre informações detalhadas dos funcionários, como dados pessoais, documentos e referências a cargos. Possui integração com tabelas de vínculos e cargos que serão expandidas futuramente.
- **Gerenciamento de Fornecedores**: Controle os dados dos fornecedores, incluindo contatos, serviços prestados e outros detalhes que facilitam o gerenciamento e acompanhamento das relações.
- **Cadastro de Clientes**: Adicione informações detalhadas dos clientes, permitindo um controle mais eficiente sobre as interações e necessidades dos mesmos.
- **Emissão de Notas Fiscais**: Automatize a geração de notas fiscais utilizando uma integração com uma API externa para garantir um processo ágil e sem erros.
- **Interface Responsiva**: Uso do Bootstrap 5 para garantir uma interface de usuário moderna e responsiva, com um layout dinâmico e funcional.

## Detalhes do Cadastro de Funcionários e Vínculos Empregatícios

Abaixo estão imagens e detalhes que ilustram o funcionamento do cadastro de funcionários:

### Exemplo de Dashboard

![Dashboard](https://github.com/MarcosSerra1/unigestao2.0/blob/main/static/image/imagens_sistema/dashboard.png)

### Formulário de Cadastro

O formulário de cadastro de funcionários é dividido em seções para facilitar a organização:

1. **Dados Pessoais**
   ![Dados Pessoais](https://github.com/MarcosSerra1/unigestao2.0/blob/main/static/image/imagens_sistema/cadastro_funcionarios_01.png)

2. **Naturalidade**
   ![Naturalidade](https://github.com/MarcosSerra1/unigestao2.0/blob/main/static/image/imagens_sistema/cadastro_funcionarios_02.png)

3. **Documentos**
   ![Documentos](https://github.com/MarcosSerra1/unigestao2.0/blob/main/static/image/imagens_sistema/cadastro_funcionarios_03.png)

4. **Carteira de Trabalho**
   ![Carteira de Trabalho](https://github.com/MarcosSerra1/unigestao2.0/blob/main/static/image/imagens_sistema/cadastro_funcionarios_04.png)

5. **Dados Complementares**
   ![Dados Complementares](https://github.com/MarcosSerra1/unigestao2.0/blob/main/static/image/imagens_sistema/cadastro_funcionarios_05.png)

6. **Contato**
   ![Contato](https://github.com/MarcosSerra1/unigestao2.0/blob/main/static/image/imagens_sistema/cadastro_funcionarios_06.png)

### Exemplo de Funcionário Cadastrado

Após o cadastro, os funcionários podem ser visualizados em uma lista:

![Funcionário Cadastrado](https://github.com/MarcosSerra1/unigestao2.0/blob/main/static/image/imagens_sistema/listagem_funcionarios.png)

## Gerenciamento de Vínculos (Bond)

O app **Bond** foi criado para gerenciar os vínculos empregatícios de forma eficiente, centralizando informações sobre contratos, cargos e relações trabalhistas. Ele é essencial para organizar os dados estruturais que impactam diretamente em outros apps, como **Employees** e **Payroll**.

### Principais Funcionalidades

- **Cadastro de Vínculos**: Permite registrar os vínculos empregatícios de cada funcionário, incluindo cargo, data de início, e término (se aplicável).
- **Histórico de Vínculos**: Acompanhe todas as alterações de vínculos ao longo do tempo, garantindo rastreabilidade.
- **Relação com Cargos**: Integra-se com o app **Employees** para vincular cargos e outras informações relevantes de cada funcionário.
<!-- - **Gerenciamento de Contratos**: Facilita a geração e o controle de contratos de trabalho personalizados para cada vínculo. (**EM DESENVOLVIMENTO**) -->

### Benefícios do App Bond

- **Organização Centralizada**: Agrupa as informações sobre vínculos em um único local, simplificando a gestão.
- **Integração com Outros Apps**: Proporciona dados consistentes para os app **Payroll**, automatizando processos e reduzindo erros.
<!-- - **Flexibilidade nos Contratos**: Gera contratos específicos para cada funcionário, atendendo às demandas legais e organizacionais. -->

### Como Usar

1. **Cadastro Inicial**: Adicione os vínculos de cada funcionário com os respectivos cargos e datas.
2. **Atualizações de Vínculo**: Registre alterações de cargo ou término de vínculo diretamente pelo painel administrativo.
<!-- 3. **Geração de Contratos**: Utilize as ferramentas do app para criar contratos baseados nos dados cadastrados.(**EM DESENVOLVIMENTO**) -->

> **Nota:** O app é parte fundamental do sistema e é projetado para ser ampliado com novas funcionalidades de acordo com as necessidades do projeto.

## Gerenciamento de Pagamentos (Payroll)

O app **Payroll** foi criado para gerenciar os pagamentos de funcionários de forma eficiente e flexível. Ele centraliza as informações relacionadas a salários, adiantamentos e histórico de pagamentos, garantindo que todas as transações financeiras estejam organizadas e acessíveis.

### Principais Funcionalidades

- **Controle de Salários**: Gerencie o pagamento de salários com base nas informações de vínculo empregatício e cargo.
- **Adiantamentos**: Permite a solicitação e o gerenciamento de adiantamentos salariais, com impacto direto no cálculo dos pagamentos.
- **Histórico de Pagamentos**: Acompanhe o histórico completo de pagamentos realizados para cada funcionário, incluindo valores, datas e adiantamentos relacionados.
<!-- - **Relatórios de Pagamento**: Gere relatórios detalhados para auditorias, controle interno ou consulta. -->

### Benefícios do App Payroll

- **Automação de Cálculos**: Reduza erros manuais com a automação dos cálculos salariais e deduções.
- **Centralização de Informações**: Todas as transações financeiras relacionadas a funcionários em um único local.
- **Integração com Outros Apps**: Integra-se com os apps **Employees** e **Bond**, garantindo que as informações de cargos e vínculos estejam sempre atualizadas.

### Como Usar

1. **Configurações Iniciais**: Certifique-se de que os dados de vínculo e cargos dos funcionários estejam preenchidos nos apps `bond`.
2. **Adiantamentos**: Solicite e registre adiantamentos diretamente pelo painel administrativo.
3. **Pagamentos**: Registre os pagamentos mensais e acompanhe o impacto de adiantamentos no saldo final.

> **Nota:** O app está projetado para expandir com futuras funcionalidades, como geração de recibos.

## Gerenciamento de Arquivos (File Manager)

O app **File Manager** foi criado para gerenciar arquivos relacionados aos funcionários de forma eficiente e organizada. Ele permite o upload, armazenamento e visualização de documentos importantes, garantindo que todas as informações estejam centralizadas e acessíveis.

### Principais Funcionalidades

- **Upload de Arquivos**: Permite o upload de arquivos relacionados aos funcionários, como documentos pessoais, certificados e outros documentos relevantes.
- **Organização por Funcionário**: Cada arquivo é associado a um funcionário específico, facilitando a organização e a busca de documentos.
- **Controle de Versões**: Mantém um histórico de uploads e atualizações de arquivos, garantindo que as versões anteriores sejam preservadas.

### Benefícios do App File Manager

- **Centralização de Documentos**: Todos os documentos relacionados aos funcionários são armazenados em um único local, facilitando o acesso e a gestão.
- **Segurança e Controle**: O acesso aos arquivos é controlado pelo sistema de permissões do Django, garantindo que apenas usuários autorizados possam visualizar ou editar os documentos.
- **Integração com Outros Apps**: Integra-se com o app **Employees**, permitindo que os arquivos sejam facilmente acessados a partir do perfil de cada funcionário.

### Como Usar

1. **Upload de Arquivos**: Acesse o perfil do funcionário e utilize a seção de upload para adicionar novos documentos.
2. **Visualização e Download**: Os arquivos podem ser visualizados e baixados diretamente a partir do perfil do funcionário.
3. **Atualização de Arquivos**: Novas versões de documentos podem ser carregadas, mantendo um histórico de alterações.

> **Nota:** O app está projetado para expandir com futuras funcionalidades, como a categorização de documentos e a geração de relatórios de arquivos.

## Ferramentas Utilizadas

- **Django**: Framework principal para desenvolvimento web.
- **Bootstrap 5**: Framework CSS para estilização e design responsivo.
- **Python**: Linguagem de programação principal.
- **PostgreSQL**: Banco de dados para armazenamento eficiente de informações.

## Como Acessar o Projeto

Você pode [acessar o código fonte do projeto](https://github.com/MarcosSerra1/unigestao2.0) ou [baixá-lo](https://github.com/MarcosSerra1/unigestao2.0/archive/refs/heads/main.zip).

## Instruções para Rodar o Projeto

### Observação sobre Banco de Dados

O projeto é configurado para usar o **PostgreSQL** quando rodando dentro de containers Docker e o **SQLite** quando rodando sem Docker. Você pode alternar entre esses dois bancos de dados alterando o valor da variável `DOCKER_MODE` no arquivo de variavel `.env`.

- **Com Docker (PostgreSQL)**: Quando o Docker está em uso, o banco de dados utilizado é o PostgreSQL. Para garantir a conexão correta, a variável `DOCKER_MODE` deve ser configurada como `True`. O arquivo `.env` deve conter as configurações do banco de dados, como nome, usuário e senha.
  
- **Sem Docker (SQLite)**: Caso você não queira usar o Docker, basta configurar `DOCKER_MODE` no arquivo `.env` como `False`. Nesse caso, o projeto usará o banco de dados SQLite, que é mais simples de configurar e pode ser usado para testes rápidos ou em ambientes de desenvolvimento.

No arquivo de variáveis `.env`, o comportamento é controlado pela seguinte variável:

```bash
# ------------------------------------------------------------
# Modo Docker
# ------------------------------------------------------------
DOCKER_MODE=False
```

Se você optar por usar o PostgreSQL com Docker, basta definir as variáveis de ambiente no arquivo `.env` como `True`.

### Usando Docker

1. Certifique-se de ter o Docker e o Docker Compose instalados. Você pode [baixar o Docker aqui](https://www.docker.com/get-started).

2. Clone este repositório para o seu ambiente local.

3. Navegue até o diretório do projeto no terminal.

4. Renomeie o arquivo `.env_example` para `.env`. O arquivo já contém as variáveis de ambiente de exemplo necessárias para a configuração do banco de dados, superusuário e parâmetros gerais do Django.

5. Inicie os containers com o comando:

    ```bash
    docker-compose up --build
    ```

6. O Docker irá construir a imagem, configurar o banco de dados e iniciar o servidor Django. Você pode acessar a aplicação em seu navegador em [http://localhost](http://localhost).

---

**Observação:**  
No modo Docker, o grupo de usuários `Usuário de Nível 1` será criado automaticamente durante a inicialização do container. Não é necessário executar manualmente o comando `python manage.py create_groups`. Este grupo é responsável por gerenciar permissões, como visualizar, editar, criar e excluir dados dos aplicativos `employees` e `bond`.

Se necessário, você pode ajustar as permissões atribuídas a este grupo diretamente pelo painel administrativo do Django.

---

### Sem Docker

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

### Carregamento de Dados Iniciais

1. Inserir Dados Cadastrais e Vínculo Empregatício:
   
    Carregar dados para Gênero, Raça, Estado Civil, Deficiência, Grau de Instrução e Nacionalidade:

      ```
      python manage.py loaddata configurations/fixtures/*.json
      ```

2. Inserir Dados CBOs:

    Carregar dados para CBOs, Ocupação e Sinônimos:

     ```
     python manage.py loaddata cbos/fixtures/*.json
     ```

3. Inserir Dados Geográficos:

    Carregar dados geográficos: Países, Estados, Capitais, Cidades e Regiões:

     ```
     python manage.py loaddata geography/fixtures/*.json
     ```

4. Inicie o servidor:

    ```
    python manage.py runserver
    ```

5. Acesse a aplicação em seu navegador em [http://localhost:8000](http://localhost:8000).

## Acesso Inicial e Segurança

Assim que o sistema estiver rodando, **é necessário acessar com um superusuário** para configurar o sistema. Para evitar que usuários regulares possam apagar dados sensíveis ou realizar alterações indevidas, recomenda-se a criação de grupos com permissões específicas.

### Recomendações de Grupos de Usuários

- **Usuário de Nível 1**: Este grupo terá acesso apenas aos apps `employees` e `bond`, que são responsáveis pelo gerenciamento de funcionários e vínculos. Usuários desse grupo podem visualizar e acessar esses dados sem riscos de interferir em outras configurações do sistema.

- **Criar Grupo Automaticamente**: Para criar o grupo automaticamente você pode usar o seguinte comando `python manage.py create_groups` esse comando chamará um script para criar o grupo e associar as permissões a ele.

Esta organização ajuda a proteger os dados, garantindo que o sistema seja utilizado de forma mais segura e eficiente, especialmente em ambientes com múltiplos usuários.

## Próximas Funcionalidades

Os próximos passos no desenvolvimento do **Uni Gestão** incluem:

- **Gerenciamento de Pagamentos**:  
  - Controle detalhado de pagamentos atrasados, adiantados e quitados.
  - Geração de relatórios financeiros.

- **Geração Automática de Contratos**:  
  - Ferramenta para criação de contratos personalizados.
  - Modelos reutilizáveis para diferentes situações empresariais.

Essas implementações garantirão maior eficiência e automação dos processos.

## Sobre o Desenvolvedor

| [<img loading="lazy" src="https://avatars.githubusercontent.com/u/78652932?v=4" width=115><br><sub>Marcos Serra</sub>](https://github.com/MarcosSerra1) |
| :---: |
| **Marcos Serra** - Desenvolvedor principal do projeto, responsável pela arquitetura e desenvolvimento das funcionalidades principais. |
