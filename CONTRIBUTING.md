# Contribuindo para o Uni Gestão

Obrigado por seu interesse em contribuir para o **Uni Gestão**! Este guia tem como objetivo orientar você no processo de contribuição para que possamos trabalhar de forma organizada e eficiente.

## Antes de Começar

### 1. **Verifique as Issues Existentes**
Antes de começar a trabalhar em uma nova feature ou bug, consulte as issues abertas para ver se alguém já está trabalhando nela ou se ela já foi resolvida. Se não houver uma issue relacionada ao que você quer fazer, **crie uma nova issue** detalhando o que você deseja adicionar ou corrigir.

### 2. **Fork e Clone do Repositório**
- Faça um **fork** do repositório para sua conta no GitHub. Isso cria uma cópia do projeto para você trabalhar.
- Clone o repositório para o seu ambiente local com o comando:
  ```bash
  git clone https://github.com/seu-usuario/uni-gestao.git
  ```

### 3. **Criação de Branch**
Crie uma branch para a sua tarefa ou correção. Use nomes de branches descritivos para indicar claramente a natureza do trabalho. Por exemplo:
- Para uma correção de bug: `fix/erro-login`
- Para uma nova funcionalidade: `feat/emissao-nota-fiscal`

Crie a branch com o comando:
```bash
git checkout -b nome-da-branch
```

### 4. **Estilo de Código**
Siga as convenções de estilo de código já estabelecidas no projeto. O código do **Uni Gestão** segue os seguintes padrões:
- **Python**: PEP 8.
- **HTML/CSS**: Utilize indentação de 2 espaços e evite usar `inline styles`. Tente seguir as convenções de boas práticas para acessibilidade.
- **Django**: Use os padrões recomendados pela documentação oficial do Django.

### 5. **Testes**
Antes de enviar suas mudanças, verifique se todos os testes estão passando. O **Uni Gestão** tem uma suíte de testes para garantir que a aplicação funcione corretamente. Você pode rodar os testes com o comando:
```bash
python manage.py test
```

Se você estiver implementando uma nova funcionalidade, adicione testes para cobrir o comportamento da nova feature. Se estiver corrigindo um bug, certifique-se de que o erro esteja coberto por um teste.

## Fazendo o Pull Request

1. **Sincronize seu Fork**
   Certifique-se de que seu fork está atualizado com a versão mais recente do repositório original. Para isso, adicione o repositório original como um remoto:
   ```bash
   git remote add upstream https://github.com/MarcosSerra1/unigestao2.0.git
   ```
   E puxe as atualizações mais recentes:
   ```bash
   git fetch upstream
   git checkout main
   git merge upstream/main
   ```

2. **Envie o Pull Request (PR)**
   Após realizar suas mudanças e testá-las, envie um pull request (PR) para o repositório principal. Descreva claramente:
   - O que foi alterado.
   - O motivo da mudança (ou o bug que foi corrigido).
   - Quais testes foram realizados.

3. **Revisão do PR**
   A equipe do projeto irá revisar seu pull request. Se necessário, podemos pedir ajustes ou melhorias. Após a aprovação, seu PR será mesclado!

## Relatando Bugs

Para relatar um bug, siga estas etapas:

1. **Verifique se o bug já foi reportado.**
2. **Crie uma issue detalhada** usando o template de "Bug", incluindo:
   - Descrição do bug.
   - Passos para reproduzir.
   - Comportamento esperado e comportamento atual.
   - Logs de erro (se houver).
   - Informações sobre o ambiente (sistema operacional, navegador, versão do sistema).
3. Se possível, forneça uma captura de tela ou gravação de vídeo para ilustrar o problema.

## Como Contribuir com Novas Funcionalidades

1. **Proponha a funcionalidade**: Antes de começar a trabalhar em uma nova funcionalidade, crie uma issue explicando a proposta. Assim podemos discutir se a funcionalidade é viável e como ela deve ser implementada.
2. **Implemente a funcionalidade**: Siga as diretrizes de desenvolvimento e crie testes adequados para garantir que a funcionalidade seja estável.
3. **Envia o PR**: Após implementar, envie um pull request explicando o que foi feito, como funciona e o impacto da funcionalidade.

## Boas Práticas de Commit

- Faça **commits pequenos e frequentes**. Isso facilita a revisão e a compreensão das mudanças.
- Use mensagens de commit claras e objetivas. Exemplo:
  - `fix: corrigido erro de login no sistema`
  - `feat: adicionada funcionalidade de emissão de notas fiscais`

## Licença

O projeto **Uni Gestão** é licenciado sob a [MIT License](LICENSE), e qualquer contribuição deve seguir os termos dessa licença.
