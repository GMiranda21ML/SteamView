Cypress.Commands.add('logar', () => {
  cy.visit('http://127.0.0.1:8000/login/');  
  cy.get('#username').type('Teste Cypress'); 
  cy.get('#password').type('123456');  
  cy.get('button').click();  
});

Cypress.Commands.add('pesquisar', (jogo) => {
  cy.visit('http://127.0.0.1:8000/');
  cy.get('.search-bar').type(jogo);
  cy.get('.search-button').click();
  cy.wait(2000);
});

describe('Search Bar -> Funcionalidade de pesquisar por jogos', () => {

  before(() => {
    cy.logar(); 
  });

  it('Cenario 1: Pesquisar um jogo com o nome correto', () => {
    cy.pesquisar('Elden Ring');
  });

  it('Cenario 2: Pesquisar um jogo inexistente', () => {
    cy.logar();
    cy.pesquisar('////////////////////////');
  });

  it('Cenario 3: Pesquisar o nome do jogo errado', () => {
    cy.logar();
    cy.pesquisar('eld ring');
  });

})