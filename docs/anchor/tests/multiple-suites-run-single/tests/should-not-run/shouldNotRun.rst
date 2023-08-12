tests/multiple-suites-run-single/tests/should-not-run/shouldNotRun.ts
=====================================================================

Last edited: 2022-12-14 20:15:57

Contents:

.. code-block:: ts

    describe("multiple-suites-run-single", () => {
  it("Should not be executed", async () => {
    throw new Error("This test has to be skipped");
  });
});


