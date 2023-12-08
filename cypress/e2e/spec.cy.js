describe("form submit", () => {
  beforeEach(() => {
    cy.visit(Cypress.env("APP_URL"));
  });

  it("submit with builtin submit", () => {
    cy.get("#systolic").type(120);
    cy.get("#diastolic").type(80);
    cy.get("form").submit();
    cy.contains("Ideal").should("be.visible");
  });

  it("submit with button click", () => {
    cy.get("#systolic").type(120);
    cy.get("#diastolic").type(80);
    cy.get("[type='submit']").click();
  });
});
