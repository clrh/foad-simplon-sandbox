describe("Roman", function() {

  it("test_test", function() {
    expect(true).toEqual(true);
  });

  it("I_donne_1", function() {
    expect(romanDonneChiffre("I")).toEqual(1);
  });

  it("V_donne_5", function() {
    expect(romanDonneChiffre("V")).toEqual(5);
  });

});
