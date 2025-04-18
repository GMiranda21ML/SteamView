describe('template spec', () => {
  it('passes', () => {
    cy.visit('http://127.0.0.1:8000/login/');
    cy.wait(1000);
    cy.contains('a', 'Cadastre-se').click();
  })
})