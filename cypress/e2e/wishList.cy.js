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

Cypress.Commands.add('addJogo', () => {
  cy.visit('http://127.0.0.1:8000/');
  cy.get('.search-bar1').type('Elden Ring');
  cy.get('.search-button').click();
  cy.wait(1000);
  cy.get('.adicionar-button').click();
  cy.wait(1000);
});

Cypress.Commands.add('visualizar', () => {
  cy.visit('http://127.0.0.1:8000/');
  cy.get('.wishList').click();
  cy.wait(2000);
});

Cypress.Commands.add('removerJogos', () => {
  cy.visit('http://127.0.0.1:8000/');
  cy.get('.wishList').click();
  cy.wait(1000);
  cy.get('.wishlist-remove').click();
  cy.wait(500);
});

Cypress.Commands.add('visualizar', () => {
  cy.visit('http://127.0.0.1:8000/');
  cy.get('.wishList').click();
  cy.wait(2000);
});

describe('O usuario pode guardar os jogos em uma WishList', () => {

  before(() => {
    cy.deleteUsers();
    cy.criarUser();
    cy.logar(); 
  });


  it('Cenario 1: Adicionar um jogo à wishlist', () => {
    cy.addJogo();
  });

  it('Cenario 2: Visualizar os jogos na wishlist', () => {
    cy.logar();
    cy.visualizar();
  });

  it('Cenario 3: Remover um jogo da wishlist', () => {
    cy.logar();
    cy.removerJogos();
  });

  it('Cenario 4: Visualizar os jogos na wishlist mas não possui nenhum jogo', () => {
    cy.logar();
    cy.visualizar();
  });

})