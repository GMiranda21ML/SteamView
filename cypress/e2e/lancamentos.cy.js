Cypress.Commands.add('logar', () => {
  cy.visit('http://127.0.0.1:8000/login/');  
  cy.get('#username').type('Teste Cypress'); 
  cy.get('#password').type('123456');  
  cy.get('button').click();  
});

Cypress.Commands.add('lancamentos', () => {
  cy.visit('http://127.0.0.1:8000/');
  cy.wait(1000);
  cy.get('.lancamentos').click();
});


describe('Visualizar os lançamentos dos jogos', () => {

  before(() => {
    cy.logar(); 
  });

  it('Cenario 1: Visualizar os lançamentos dos jogos com sucesso', () => {
    cy.lancamentos();
  })
})