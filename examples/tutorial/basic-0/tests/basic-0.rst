examples/tutorial/basic-0/tests/basic-0.js
==========================================

Last edited: 2022-12-14 20:15:57

Contents:

.. code-block:: js

    const anchor = require("@project-serum/anchor");

describe("basic-0", () => {
  // Configure the client to use the local cluster.
  anchor.setProvider(anchor.AnchorProvider.local());

  it("Uses the workspace to invoke the initialize instruction", async () => {
    // #region code
    // Read the deployed program from the workspace.
    const program = anchor.workspace.Basic0;

    // Execute the RPC.
    await program.methods.initialize().rpc();
    // #endregion code
  });
});


