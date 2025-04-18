Cypress.Commands.add('deleteUsers', () => {
  const pythonPath = '"C:\\Program Files\\Python39\\python.exe"'; 
  const scriptPath = '"C:\\Gabriel Lima\\faculdade\\Cesar\\FDS\\SteamView\\delete_users.py"';
  cy.exec(`${pythonPath} ${scriptPath}`).then((result) => {
    console.log(result.stdout); 
    if (result.stderr) {
      console.error(result.stderr);
    }
  });
});

Cypress.Commands.add('criarUser', () => {
  cy.visit('http://127.0.0.1:8000/login/');
  cy.contains('a', 'Cadastre-se').click();
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

describe('User flow', () => {

  before(() => {
    cy.deleteUsers(); 
  });

  it('deve criar um usuario e fazer login no site', () => {
    cy.criarUser(); 
    cy.logar(); 
  });
});
