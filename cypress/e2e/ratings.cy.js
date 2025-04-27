Cypress.Commands.add('logar', () => {
  cy.visit('http://127.0.0.1:8000/login/');  
  cy.get('#username').type('Teste Cypress'); 
  cy.get('#password').type('123456');        
  cy.get('button').click();                  
});

Cypress.Commands.add('visualizar', () => {
  cy.visit('http://127.0.0.1:8000/');       
  cy.get('.ratings').click();   
  cy.wait(1000);
  cy.get('#load-more').click();                  
});

Cypress.on('uncaught:exception', (err, runnable) => {
  return false;
});

describe('Mostrar as avaliações dos jogos', () => {

  before(() => {
    cy.logar();  
  });

  it('Visualizar as avaliações dos jogos', () => {
    cy.visualizar();  
  });

});
