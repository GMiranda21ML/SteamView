Cypress.Commands.add('deleteUsers', () => {
  cy.exec('python delete_users.py', { failOnNonZeroExit: false }).then((result) => {
    console.log(result.stdout); 
    if (result.stderr) {
      console.error(result.stderr);
    }
  });
});

Cypress.Commands.add('criarUser', () => {
  cy.visit('http://127.0.0.1:8000/login/');
  cy.wait(1000);
  cy.contains('a', 'CADASTRE-SE').click();
  cy.get('#username').type('Teste Cypress'); 
  cy.get('#email').type('testeCypress@gmail.com'); 
  cy.get('#password1').type('123456'); 
  cy.get('#password2').type('123456'); 
  cy.get('button').click();
});

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
    cy.deleteUsers();
    cy.criarUser();
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