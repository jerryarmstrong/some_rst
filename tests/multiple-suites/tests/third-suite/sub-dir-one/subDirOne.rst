tests/multiple-suites/tests/third-suite/sub-dir-one/subDirOne.ts
================================================================

Last edited: 2022-12-14 20:15:57

Contents:

.. code-block:: ts

    import * as anchor from "@project-serum/anchor";
import { Program } from "@project-serum/anchor";
import { PublicKey } from "@solana/web3.js";
import { MultipleSuites } from "../../../target/types/multiple_suites";
import { assert } from "chai";

describe("multiple-suites", () => {
  // Configure the client to use the local cluster.
  anchor.setProvider(anchor.AnchorProvider.env());

  const program = anchor.workspace.MultipleSuites as Program<MultipleSuites>;

  it("Is initialized!", async () => {
    // Add your test here.
    const tx = await program.rpc.initialize(new anchor.BN(347234), {});

    // SOME_TOKEN.json should exist.
    const SOME_TOKEN = await program.provider.connection.getAccountInfo(
      new PublicKey("C4XeBpzX4tDjGV1gkLsj7jJh6XHunVqAykANWCfTLszw")
    );

    // SOME_ACCOUNT.json should NOT exist.
    const SOME_ACCOUNT = await program.provider.connection.getAccountInfo(
      new PublicKey("3vMPj13emX9JmifYcWc77ekEzV1F37ga36E1YeSr6Mdj")
    );

    assert.isNotNull(SOME_TOKEN);
    assert.isNull(SOME_ACCOUNT);

    console.log("Your transaction signature", tx);
  });
});


