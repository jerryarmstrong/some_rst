tests/typescript/tests/typescript.spec.ts
=========================================

Last edited: 2022-12-14 20:15:57

Contents:

.. code-block:: ts

    import * as anchor from "@project-serum/anchor";

describe("typescript", () => {
  // Configure the client to use the local cluster.
  anchor.setProvider(anchor.AnchorProvider.env());

  it("Is initialized!", async () => {
    // Add your test here.
    const program = anchor.workspace.Typescript;
    const tx = await program.rpc.initialize();
    console.log("Your transaction signature", tx);
  });
});


