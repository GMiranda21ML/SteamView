# SteamView

## 📖 Descrição
O SteamView é um software feito pelo framework Django, tem como objetivo ajudar jogadores que buscam analisar informações dos jogos da steam, como por exemplo, ver descontos em jogos, os jogos mais vendidos, os mais bem avaliados, requisitos de software, entre outros.

---

## 🧑‍💻 Tecnologias e Ferramentas
- framework Django: Django é um framework web em Python que permite o desenvolvimento rápido e seguro de aplicações, seguindo o padrão MVT. Ele inclui uma ORM poderosa, autenticação integrada e painel administrativo automático.
- Figma: Figma é uma ferramenta de design colaborativo baseada na web, usada para criar interfaces, protótipos e designs. Permite trabalho em tempo real, facilitando a colaboração entre equipes.
- Jira: O Jira é uma ferramenta para gerenciar tarefas e projetos, especialmente em equipes de software, usando metodologias ágeis.

---

<details>
<summary>🔗 LINKS IMPORTANTES</summary>

<div align="center">
    <a href="https://steamviewfds.atlassian.net/jira/software/projects/SCRUM/boards/1?atlOrigin=eyJpIjoiMjZiNDgyNDQxMGM4NGYzZGE2OWVmM2YyM2EyYjUwODYiLCJwIjoiaiJ9">
        <img src="https://img.shields.io/badge/Jira-0052CC?style=for-the-badge&logo=Jira&logoColor=white" alt="Jira">
    </a>
    <a href="https://docs.google.com/document/d/1S2g1G4RuujxoqrS3X8qtjB-jPXst8eDhbwKny189anE/edit?tab=t.0">
        <img src="https://img.shields.io/badge/Google%20Docs-4285F4?style=for-the-badge&logo=Google-Docs&logoColor=white" alt="Google Docs">
    </a>
    <a href="https://www.figma.com/design/3nPg7kwxtVKxKwypslPQtB/SteamView?node-id=58-582&t=77d8WioUx6bMMnMa-1">
        <img src="https://img.shields.io/badge/Figma-4B0082?style=for-the-badge&logo=Figma&logoColor=white" alt="Figma">
    </a>
    <a href="https://steam-view.azurewebsites.net">
        <img src="https://img.shields.io/badge/Steamview-007BFF?style=for-the-badge&logo=firefox&logoColor=white" alt="Screencast">
    </a>
</div>

</details>

---

<details>
<summary>📝 PRIMEIRA ENTREGA</summary>

O objetivo deste sprint é estabelecer a infraestrutura inicial do sistema, com foco em funcionalidades essenciais para o gerenciamento de usuários. 

Será implementada a análise do ranking de jogos mais jogados, pesquisa específica do jogo desejado para saber mais sobre o mesmo, a comparação do meu hardware com os requisitos mínimos do jogo em questão. 

Também será possível analisar melhores descontos dos jogos, analisar as notas/avaliações dos jogos, analisar detalhes do jogo desejado, analisar lançamentos populares, analisar jogos mais e menos vendidos.

Juntamente com a entrega do layout das histórias criadas pelo Figma e atualização do backlog no Jira. Também criamos um Screencast, para apresentar o nosso protótipo de baixa fidelidade feito pelo figma, acesse  e um criamos um docs com as histórias para registrar as mesmas, acesse 

Juntamente com a entrega do layout das histórias criadas no Figma e a atualização do backlog no Jira, também produzimos um Screencast para apresentar nosso protótipo de baixa fidelidade desenvolvido no Figma. Você pode acessá-lo [clicando aqui](https://www.youtube.com/watch?v=4X-COxfohOs). Além disso, criamos um documento para registrar todas as histórias. Para acessá-lo, [clique aqui](https://docs.google.com/document/d/1S2g1G4RuujxoqrS3X8qtjB-jPXst8eDhbwKny189anE/edit?tab=t.0").

Nosso figma contem 8 telas que se resumem a login, cadastro, menu de pesquisa, rankings, promoções, avaliações, mais vendidos e sobre o jogo:
![figma](img/Figma.png)

O jira ficou com a criação do backlog com atualização da primeira sprint, juntamente com o quadro com as infomações que serão atualizadas no futuro do projeto:
![Backlog](img/Backlog.png)

![Quadro](img/Quadro.png)


</details>

---

<details>
<summary>📝 SEGUNDA ENTRAGA </summary>

O objetivo desta segunda sprint é começar a fazer o projeto de verdade, implementando nossas primeiras histórias de usuário na prática.


## Histórias implementadas:


1. Pesquisa de jogos, que permite ao usuário encontrar jogos específicos por meio do nome do jogo.


![Searchbar](img/Telasearchbar.png)


2. Exibição de detalhes dos jogos, permitindo que o usuário consiga ver mais informações a respeito do título pesquisado.




![Informacoesjogos](img/Telajogo.png)




3. Exibição da avaliação dos jogos, o que permite ao usuário ter uma noção mais clara do feedback da comunidade a respeito de determinado jogo.



![RatingJogos](img/Ratings.png)

# Jira


Trouxemos uma atualização do backlog no Jira, que é por onde conseguimos gerenciar o andamento do projeto e organizar as demandas e histórias, onde implementamos essas 3 histórias.Para acessá-lo, [clique aqui](https://steamviewfds.atlassian.net/jira/software/projects/SCRUM/boards/1?atlOrigin=eyJpIjoiMjZiNDgyNDQxMGM4NGYzZGE2OWVmM2YyM2EyYjUwODYiLCJwIjoiaiJ9).

BackLog:

![Jira](img/Backlogjiraentrega2.png)

Board:

![Jira](img/Boardjiraentrega2.png)


# Screencast
Além disso, trouxemos, desta vez, um screencast para apresentar o nosso projeto - agora já desenvolvido em Django. Você pode acessá-lo [clicando aqui](https://youtu.be/1OVcVGjYgdY). Além disso, criamos um documento para relatar como foram divididas as tarefas entre o grupo. Para acessá-lo, [clique aqui](https://steam-view.azurewebsites.net).

# Bugtracker
Fizemos a criação de um bugtracker, onde podemos ver a correção de bugs e melhorias no Steam View.

![Issues](img/Issues.png)

Bugs corrigidos:


1. Bug de redirecionamento de tela:


- Antes, o usuário era redirecionado de forma errada. Ele ia para uma tela onde era para aparecer o jogo antes de pesquisá-lo, o que, após essa correção, foi ajeitado e agora o usuário é direcionado primeiramente para a barra de pesquisa e depois para as informações do jogo.




2. Bug de repetição de jogos no banco de dados:


- O código, antes, não verificava se o jogo existia no banco de dados e o criava repetido. Agora ocorre a verificação e, caso não esteja, é criado no banco.




Melhorias:


1. Mudança na API atualizada:


- Alteração da API da Steam pela API da RAWG, com o intuito de melhorar a funcionalidade do site, já que a API da Steam se encontrava desatualizada, assim, não trazendo as informações solicitadas de jogos mais recentes ou trazendo informações desatualizadas.



2. Edição do redirecionamento para o login:


- Caso o usuário não esteja logado, é redirecionado automaticamente para a tela de login.

# Relatório

Criamos um documento para relatar como foram dividas as tarefas entre o grupo.Para acessá-lo, [clique aqui](https://docs.google.com/document/d/1kGRfZ-oWasivb5I1HcR4BfNv_ETWxWy5BHzKlodHNbM/edit?usp=sharing).


</details>

---

<details>
<summary>📝 TERCEIRA ENTREGA</summary>

O objetivo desta terceira sprint foi expandir o SteamView, trazendo novas funcionalidades e melhorias gerais no sistema.


# Histórias implementadas:


## História 1: Visualizar o ranking dos 20 jogos mais jogados no mês

- Cenário 1: Visualizar o top 20 dos jogos mais jogados em ordem decrescente
  - Dado que o usuário está logado e deseja visualizar a ordem decrescente do top 20 dos jogos mais jogados;
  - Quando seleciona a aba de top 20 dos jogos mais jogados e coloca em ordem decrescente;
  - Então uma lista decrescente do top 20 dos jogos mais jogados aparecerá.

- Cenário 2: Visualizar o top 20 dos jogos mais jogados em ordem crescente
  - Dado que o usuário está logado e deseja visualizar a ordem decrescente do top 20 dos jogos mais jogados;
  - Quando seleciona a aba do top 20 dos jogos mais jogados e coloca em ordem crescente ao invés de decrescente;
  - Então uma lista crescente do top 20 dos jogos mais jogados aparecerá.

Top 20 mais jogados do mês:

![Top20Jogos](img/Top20maisjogados.png)

Top 20 menos jogados mês:

![Top20Jogos](img/Top20menosjogados.png)
---

## História 2: Visualizar lançamentos populares

- Cenário 1: Exibir jogos lançados recentemente e que estão com uma média alta de jogadores
  - Dado que o usuário deseja visualizar lançamentos populares recentes;
  - Quando ele seleciona a aba de “lançamentos”;
  - Então o site exibirá uma lista de jogos lançados recentemente e ao lado do mesmo, aparecerá a média de jogadores.

Lançamentos:

![LancamentosPopulares](img/Lancamentos.png)

---

## História 3: Visualizar jogos mais e menos jogados

- Cenário 1: Exibição dos jogos mais vendidos
  - Dado que o usuário deseja ver os jogos mais vendidos;
  - Quando ele entra na seção de jogos mais/menos vendidos e seleciona o filtro de jogos mais vendidos;
  - Então o site exibe os jogos mais jogados.

- Cenário 2: Exibição dos jogos menos vendidos
  - Dado que o usuário deseja ver os jogos menos vendidos;
  - Quando ele entra na seção de jogos mais/menos vendidos e seleciona o filtro de jogos menos vendidos;
  - Então o site exibe os jogos menos jogados.

Mais jogados:

![Maisjogados](img/Maisjogados.png)

Menos jogados:

![Menosjogados](img/Menosjogados.png)

---

# Jira


Trouxemos uma atualização do Jira, que é por onde conseguimos gerenciar o andamento do projeto e organizar as demandas e histórias, onde implementamos mais 3 histórias.Para acessá-lo, [clique aqui](https://steamviewfds.atlassian.net/jira/software/projects/SCRUM/boards/1?atlOrigin=eyJpIjoiMjZiNDgyNDQxMGM4NGYzZGE2OWVmM2YyM2EyYjUwODYiLCJwIjoiaiJ9).

BackLog:

![Jira](img/backlogEntrega3.png)

Board:

![Jira](img/painelSprint3.png)

---

# Screencast
Nesta entrega, criamos um screencast apresentando todas as novas funcionalidades, o processo de deploy, testes no Cypress, CI/CD e também o protótipo atualizado no Figma.

<div align="center">
    <a href="https://youtu.be/Uf8vVWzHc9c">
        <img src="https://img.shields.io/badge/Deploy-228B22?style=for-the-badge&logo=vercel&logoColor=white" alt="Deploy">
    </a>
    <a href="https://youtu.be/d8GGJhNQp74">
        <img src="https://img.shields.io/badge/Cypress-6E40C9?style=for-the-badge&logo=cypress&logoColor=white" alt="Cypress">
    </a>
    <a href="https://youtu.be/xRUsTvIcS2A">
        <img src="https://img.shields.io/badge/CI/CD-1E90FF?style=for-the-badge&logo=githubactions&logoColor=white" alt="CI/CD">
    </a>
    <a href="https://youtu.be/Mr5kWbItk0w">
        <img src="https://img.shields.io/badge/Figma-4B0082?style=for-the-badge&logo=Figma&logoColor=white" alt="Figma">
    </a>
</div>

---

# Bugtracker

Criamos uma nova seção de bug tracker para controle das falhas e melhorias aplicadas na nova sprint.


Open:

![Open](img/Open.png)


Closed:

![Closed](img/Closed.png)


---

# Relatório de Programação

Atualizamos o documento onde é detalhado como foram divididas as tarefas de desenvolvimento nesta entrega.

[Link para o relatório](https://docs.google.com/document/d/1kGRfZ-oWasivb5I1HcR4BfNv_ETWxWy5BHzKlodHNbM/edit?usp=sharing)

---

</details>

---

<details>
<summary>📝 QUARTA ENTREGA</summary>

"O objetivo desta terceira sprint foi expandir o SteamView, trazendo novas funcionalidades e melhorias gerais ao sistema. Além disso, optamos por remover duas histórias — a de descontos e a de hardware — e adicionar duas novas: a de wishlist e a de conteúdo aleatório (random).


# Histórias implementadas:

# 🧩 Histórias de Usuário

Este documento descreve funcionalidades esperadas para o sistema SteamView, baseadas em histórias de usuário.

---

## 📝 História 3: Wishlist

**Como** um usuário normal do site,  
**Quero** poder adicionar, remover e visualizar jogos na minha wishlist,  
**Para** que eu possa acompanhar os jogos que me interessam.

### 📌 Cenários

#### ✅ Cenário 1: Adicionar um jogo à wishlist

**Dado que** o usuário está logado e deseja adicionar um jogo à wishlist,  
**Quando** ele acessa a página de algum jogo e escolhe a opção “Adicionar à wishlist”,  
**Então** o jogo é adicionado à wishlist.

---

#### 👀 Cenário 2: Visualizar os jogos na wishlist

**Dado que** o usuário está logado e deseja ver os jogos que possui na wishlist,  
**Quando** ele vai na aba *Wishlist*,  
**Então** são exibidos os jogos que ele adicionou.

---

#### 🗑️ Cenário 3: Remover um jogo da wishlist

**Dado que** o usuário está logado e deseja remover um jogo da wishlist,  
**Quando** ele vai na aba *Wishlist* e clica em “Remover” em um jogo,  
**Então** o jogo é removido da wishlist.

---

#### ℹ️ Cenário 4: Visualizar wishlist vazia

**Dado que** o usuário está logado e deseja ver os jogos na wishlist,  
**Quando** ele vai na aba *Wishlist* e não há jogos adicionados,  
**Então** é exibida uma mensagem informando que a wishlist ainda está vazia.

---

Wishlist:

![Wishlist](img/Wishlist.png)

## 🎲 História 8: Jogo Aleatório

**Como** um usuário normal do site,  
**Quero** que o site escolha um jogo aleatoriamente por mim,  
**Para** que eu descubra jogos novos de forma divertida.

### 📌 Cenário

#### 🔀 Cenário Único: Seleção aleatória de jogo

**Dado que** o usuário está logado e deseja que o site escolha um jogo aleatoriamente por ele,  
**Quando** ele vai na aba *Random* e clica em “Pegue um jogo aleatório”,  
**Então** é exibido um jogo escolhido aleatoriamente.

Random:

![Random1](img/Random1.png)

![Random2](img/Random2.png)

---

# Jira


Trouxemos uma atualização do Jira, que é por onde conseguimos gerenciar o andamento do projeto e organizar as demandas e histórias, onde implementamos mais 2 histórias.Para acessá-lo, [clique aqui](https://steamviewfds.atlassian.net/jira/software/projects/SCRUM/boards/1?atlOrigin=eyJpIjoiMjZiNDgyNDQxMGM4NGYzZGE2OWVmM2YyM2EyYjUwODYiLCJwIjoiaiJ9).

BackLog:

![Backlog](img/jiraquarta1.png)

Board:

![Board](img/jiraquarta2.png)

Arquivadas:

![Arquivadas](img/jiraquarta3.png)
---

# Screencast
Nesta entrega, criamos um screencast apresentando todas as novas funcionalidades, o processo de deploy, testes no Cypress, CI/CD e também o protótipo atualizado no Figma.

<div align="center">
    <a href="https://youtu.be/dvkuvooATQU">
        <img src="https://img.shields.io/badge/Deploy-228B22?style=for-the-badge&logo=vercel&logoColor=white" alt="Deploy">
    </a>
    <a href="https://youtu.be/17q64bXPpaU">
        <img src="https://img.shields.io/badge/Cypress-6E40C9?style=for-the-badge&logo=cypress&logoColor=white" alt="Cypress">
    </a>
    <a href="https://youtu.be/F3JNfzYbGrY">
        <img src="https://img.shields.io/badge/CI/CD-1E90FF?style=for-the-badge&logo=githubactions&logoColor=white" alt="CI/CD">
    </a>
    <a href="https://youtu.be/DPz4at2zR2I">
        <img src="https://img.shields.io/badge/Figma-4B0082?style=for-the-badge&logo=Figma&logoColor=white" alt="Figma">
    </a>
</div>

---

# Bugtracker

Criamos uma nova seção de bug tracker para controle das falhas e melhorias aplicadas na nova sprint.


Open:

![Open](img/Openquarta.png)

Closed:

![Closed](img/closedquarta.png)


---

# Relatório de Programação

Atualizamos o documento onde é detalhado como foram divididas as tarefas de desenvolvimento nesta entrega.

[Link para o relatório](https://docs.google.com/document/d/1kGRfZ-oWasivb5I1HcR4BfNv_ETWxWy5BHzKlodHNbM/edit?usp=sharing)

---

## 🫂 Integrantes
| Matricula  | Nome                                  | Email da school    |
| ---------- | ------------------------------------- | ------------------ |
| 2024200049 | André Avelino Freitas de Oliveira     | aafo@cesar.school  | 
| 2024200395 | Augusto Malheiros de Souza            | ams10@cesar.school | 
| 2024200040 | Caio Mathews de Farias Ferreira       | cmff@cesar.school  | 
| 2024200327 | Eduardo Albuquerque Alves Barbosa     | eaab@cesar.school  |
| 2024200393 | Gabriel Miranda Murcabel de Lima      | gmml@cesar.school  |
| 2024200124 | Ricardo Sérgio de Paula Freitas Filho | rspff@cesar.school |






