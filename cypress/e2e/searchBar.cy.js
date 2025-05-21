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

Cypress.Commands.add('pesquisar', (jogo) => {
  cy.visit('http://127.0.0.1:8000/');
  cy.get('.search-bar1').type(jogo);
  cy.get('.search-button').click();
  cy.wait(2000);
});

describe('Search Bar -> Funcionalidade de pesquisar por jogos', () => {

  before(() => {
    cy.deleteUsers();
    cy.criarUser();
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