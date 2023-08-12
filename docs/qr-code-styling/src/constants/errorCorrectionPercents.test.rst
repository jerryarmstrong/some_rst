src/constants/errorCorrectionPercents.test.js
=============================================

Last edited: 2023-05-04 20:47:44

Contents:

.. code-block:: js

    import errorCorrectionPercents from "./errorCorrectionPercents";

describe("Error Correction Percents", () => {
  it("The export of the module should be an object", () => {
    expect(typeof errorCorrectionPercents).toBe("object");
  });

  it.each(Object.values(errorCorrectionPercents))("Values should be numbers", value => {
    expect(typeof value).toBe("number");
  });

  it.each(Object.keys(errorCorrectionPercents))("Allowed only particular keys", key => {
    expect(["L", "M", "Q", "H"]).toContain(key);
  });
});


