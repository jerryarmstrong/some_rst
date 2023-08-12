tests/nft-voter.ts
==================

Last edited: 2023-06-01 19:30:16

Contents:

.. code-block:: ts

    import * as anchor from "@project-serum/anchor";
import { Program } from "@project-serum/anchor";
import { NftVoter } from "../target/types/nft_voter";

describe("nft-voter", () => {

  const program = anchor.workspace.NftVoter as Program<NftVoter>;

  it("Is initialized!", async () => {

    const records = program.account.nftVoteRecord.all();
    // Add your test here.
    //const tx = await program.rpc.createRegistrar({});
    console.log("Your transaction signature", records);
  });
});


