tests/multiple-suites/tests/fourth-and-fifth-suite/forth-suite/forth-suite.ts
=============================================================================

Last edited: 2022-12-14 20:15:57

Contents:

.. code-block:: ts

    import * as anchor from "@project-serum/anchor";
import { Program } from "@project-serum/anchor";
import { PublicKey } from "@solana/web3.js";
import { assert } from "chai";
import { MultipleSuites } from "../../../target/types/multiple_suites";

describe("multiple-suites", () => {
  // Configure the client to use the local cluster.
  anchor.setProvider(anchor.AnchorProvider.env());

  const program = anchor.workspace.MultipleSuites as Program<MultipleSuites>;

  it("Is initialized!", async () => {
    // Add your test here.
    const tx = await program.rpc.initialize(new anchor.BN(34823), {});

    // SOME_TOKEN.json should exist.
    const SOME_TOKEN = await program.provider.connection.getAccountInfo(
      new PublicKey("C4XeBpzX4tDjGV1gkLsj7jJh6XHunVqAykANWCfTLszw")
    );

    // SOME_ACCOUNT.json should NOT exist.
    const SOME_ACCOUNT = await program.provider.connection.getAccountInfo(
      new PublicKey("3vMPj13emX9JmifYcWc77ekEzV1F37ga36E1YeSr6Mdj")
    );

    // ANOTHER_ACC.json should exist.
    const ANOTHER_ACC = await program.provider.connection.getAccountInfo(
      new PublicKey("JC7Vcye5upE6tMLAjAem76MCGuPNidTtg2cuYm71UukH")
    );

    // CLONED ACC should exist.
    const CLONED_ACC = await program.provider.connection.getAccountInfo(
      new PublicKey("metaqbxxUerdq28cj1RbAWkYQm3ybzjb6a8bt518x1s")
    );

    assert.isNotNull(SOME_TOKEN);
    assert.isNull(SOME_ACCOUNT);
    assert.isNotNull(ANOTHER_ACC);
    assert.isNotNull(CLONED_ACC);
    console.log("Your transaction signature", tx);
  });
});


