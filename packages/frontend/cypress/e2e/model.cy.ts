// https://on.cypress.io/api

describe('Model', () => {
  it('the model has the adequate title', () => {
    cy.visit('/')
    cy.contains('h2', '¿Tienes problemas para entender el mercado de la publicidad digital? ')
  });

  it('visits the app root url', () => {
    cy.visit('/')
    cy.contains('h2', '¿Tienes problemas para entender el mercado de la publicidad digital? ')
  });
});
