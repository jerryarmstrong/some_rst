packages/app-extension/src/utils/solana.ts
==========================================

Last edited: 2023-07-01 03:20:04

Contents:

.. code-block:: ts

    import type { SolanaFeeConfig } from "@coral-xyz/common";
import {
  Blockchain,
  deserializeLegacyTransaction,
  deserializeTransaction,
} from "@coral-xyz/common";
import { ComputeBudgetProgram } from "@solana/web3.js";
import { ethers } from "ethers";

const { base58: bs58 } = ethers.utils;

export const sanitizeTransactionWithFeeConfig = (
  txStr: string,
  blockchain: Blockchain,
  feeConfig?: { disabled: boolean; config: SolanaFeeConfig }
) => {
  if (
    blockchain === Blockchain.SOLANA &&
    feeConfig &&
    feeConfig?.config.priorityFee &&
    !feeConfig.disabled
  ) {
    let tx = deserializeTransaction(txStr);

    if (tx.version === "legacy") {
      return txStr;
    }

    const transaction = deserializeLegacyTransaction(txStr);
    const modifyComputeUnits = ComputeBudgetProgram.setComputeUnitLimit({
      units: feeConfig.config.computeUnits,
    });

    const addPriorityFee = ComputeBudgetProgram.setComputeUnitPrice({
      microLamports: feeConfig.config.priorityFee,
    });

    transaction.add(modifyComputeUnits);
    transaction.add(addPriorityFee);
    return bs58.encode(
      transaction.serialize({
        requireAllSignatures: false,
        verifySignatures: false,
      })
    );
  } else {
    return txStr;
  }
};


