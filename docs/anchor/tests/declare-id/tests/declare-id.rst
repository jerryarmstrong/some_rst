tests/declare-id/tests/declare-id.ts
====================================

Last edited: 2022-12-14 20:15:57

Contents:

.. code-block:: ts

    import * as anchor from "@project-serum/anchor";
import { AnchorError, Program } from "@project-serum/anchor";
import splToken from "@solana/spl-token";
import { DeclareId } from "../target/types/declare_id";
import { assert } from "chai";

describe("declare_id", () => {
  anchor.setProvider(anchor.AnchorProvider.local());
  const program = anchor.workspace.DeclareId as Program<DeclareId>;

  it("throws error!", async () => {
    try {
      await program.methods.initialize().rpc();
      assert.ok(false);
    } catch (_err) {
      assert.isTrue(_err instanceof AnchorError);
      const err: AnchorError = _err;
      assert.strictEqual(err.error.errorCode.number, 4100);
    }
  });
});


