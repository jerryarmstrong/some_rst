examples/tutorial/basic-0/client.js
===================================

Last edited: 2022-12-14 20:15:57

Contents:

.. code-block:: js

    // client.js is used to introduce the reader to generating clients from IDLs.
// It is not expected users directly test with this example. For a more
// ergonomic example, see `tests/basic-0.js` in this workspace.

const anchor = require("@project-serum/anchor");

// Configure the local cluster.
anchor.setProvider(anchor.AnchorProvider.local());

async function main() {
  // #region main
  // Read the generated IDL.
  const idl = JSON.parse(
    require("fs").readFileSync("./target/idl/basic_0.json", "utf8")
  );

  // Address of the deployed program.
  const programId = new anchor.web3.PublicKey("<YOUR-PROGRAM-ID>");

  // Generate the program client from IDL.
  const program = new anchor.Program(idl, programId);

  // Execute the RPC.
  await program.rpc.initialize();
  // #endregion main
}

console.log("Running client.");
main().then(() => console.log("Success"));


