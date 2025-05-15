Cypress.Commands.add('logar', () => {
  cy.visit('http://127.0.0.1:8000/login/');  
  cy.get('#username').type('Teste Cypress'); 
  cy.get('#password').type('123456');  
  cy.get('button').click();  
});

Cypress.Commands.add('randomChoose', () => {
  cy.visit('http://127.0.0.1:8000/');
  cy.get('.random').click();
  cy.wait(1000);
  cy.get('.random-button').click();
  cy.wait(1000);
  cy.get('.random-button').click();
  cy.wait(1000);
  cy.get('.random-button').click();
  cy.wait(1000);

});

describe('Um jogo aleatorio aparece para o usuario como recomendação', () => {

  before(() => {
    cy.logar(); 
  });

  it('Cenario 1: a pessoa clica no botão e gera um jogo aleatorio', () => {
    cy.randomChoose();
  })
})