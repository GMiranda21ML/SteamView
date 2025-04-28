Cypress.Commands.add('logar', () => {
  cy.visit('http://127.0.0.1:8000/login/');  
  cy.get('#username').type('Teste Cypress'); 
  cy.get('#password').type('123456');  
  cy.get('button').click();  
});

Cypress.Commands.add('maisJogados', () => {
  cy.visit('http://127.0.0.1:8000/');
  cy.get('.maisJogadosHist').click();
  cy.get('.filterMais').check({ force: true });
  cy.wait(1500);
});

Cypress.Commands.add('menosJogados', () => {
  cy.visit('http://127.0.0.1:8000/');
  cy.get('.maisJogadosHist').click();
  cy.get('.filterMenos').check({ force: true });
});

describe('Visualizar os jogos mais e menos jogados/populares nos ultimos 10 anos', () => {

  before(() => {
    cy.logar(); 
  });

  it('Cenario 1: Visualizar os jogos mais jogados/populares', () => {
    cy.maisJogados();
  });

  it('Cenario 2: Visualizar os jogos menos jogados/populares', () => {
    cy.logar();
    cy.menosJogados();
  });

})