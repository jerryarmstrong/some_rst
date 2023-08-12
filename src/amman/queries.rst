src/amman/queries.ts
====================

Last edited: 2022-08-30 20:54:29

Contents:

.. code-block:: ts

    import {
  Blockhash,
  BlockSignatures,
  Connection,
  TransactionSignature,
} from "@solana/web3.js";
import { strict as assert } from "assert";
import bs58 from "bs58";
import { LOCALHOST } from "./consts";
import { TransactionSignatureWithBlock } from "./types";

const voteRx = /Program Vote111111111111111111111111111111111111111/;

class BlockAgent {
  readonly connection: Connection;
  constructor(url: string) {
    this.connection = new Connection(url, "confirmed");
  }

  async getBlockIds() {
    const txCount = await this.connection.getTransactionCount();
    const firstBlockId = await this.connection.getFirstAvailableBlock();
    const blockIds = await this.connection.getBlocks(
      firstBlockId,
      firstBlockId + txCount,
      "confirmed"
    );
    return {
      firstBlockId,
      blockIds,
    };
  }

  async oldestValidBlockSignatures() {
    const { firstBlockId, blockIds } = await this.getBlockIds();
    let blockSignatures:
      | { block: number; signatures: BlockSignatures }
      | undefined = undefined;
    for (const id of blockIds.reverse()) {
      try {
        const signatures = await this.connection.getBlockSignatures(id);
        blockSignatures = { block: id, signatures };
      } catch (err: any) {}
      if (blockSignatures != null) break;
    }

    assert(blockSignatures != null, "could not find any block signatures");
    return { firstBlockId, blockIds, blockSignatures };
  }

  async latestTransactionSignatures(amount = 10): Promise<
    {
      block: number;
      signature: TransactionSignature;
      blockHash: Blockhash;
      previousBlockHash: Blockhash;
    }[]
  > {
    const { blockIds } = await this.getBlockIds();
    let allSigs = [];
    for (let slot of blockIds) {
      let blockSignatures;
      try {
        blockSignatures = await this.connection.getBlockSignatures(
          slot,
          "confirmed"
        );
      } catch (err) {
        continue;
      }
      slot = blockSignatures.parentSlot;

      for (const signature of blockSignatures.signatures.filter(
        (x) => bs58.decode(x).length === 64
      )) {
        const tx = await this.connection.getTransaction(signature);
        if (
          tx?.meta?.logMessages == null ||
          voteRx.test(tx.meta.logMessages[0])
        ) {
          continue;
        }
        allSigs.push({
          block: slot,
          signature,
          blockHash: blockSignatures.blockhash,
          previousBlockHash: blockSignatures.previousBlockhash,
        });
        if (allSigs.length >= amount) break;
      }
      if (allSigs.length >= amount) break;
    }
    return allSigs.reverse();
  }
}

export function createBlockAgent(url: string) {
  return new BlockAgent(url);
}

export async function getLatestTransactionSignatures(
  url: string = LOCALHOST,
  amount = 5
): Promise<TransactionSignatureWithBlock[]> {
  return createBlockAgent(url).latestTransactionSignatures(amount);
}


