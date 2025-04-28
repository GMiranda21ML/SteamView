Cypress.Commands.add('logar', () => {
  cy.visit('http://127.0.0.1:8000/login/');  
  cy.get('#username').type('Teste Cypress'); 
  cy.get('#password').type('123456');  
  cy.get('button').click();  
});

Cypress.Commands.add('ordemCrescente', () => {
  cy.visit('http://127.0.0.1:8000/');
  cy.get('.maisJogados').click();
  cy.get('.normalOrderButton').check({ force: true });
  cy.wait(2000)
});

Cypress.Commands.add('ordemDecrescente', () => {
  cy.visit('http://127.0.0.1:8000/');
  cy.get('.maisJogados').click();
  cy.get('.invertOrderButton').check({ force: true });
});

describe('Mostrar o Ranking do top 20 jogos mais jogados', () => {
  
  before(() => {
    cy.logar(); 
  });

  it('Cenario 1: Visualizar o ranking dos jogos mais jogados em ordem crescente', () => {
    cy.ordemCrescente();
  });

  it('Cenario 2: Visualizar o ranking dos jogos mais jogados em ordem decrescente', () => {
    cy.logar();
    cy.ordemDecrescente();
  });
})