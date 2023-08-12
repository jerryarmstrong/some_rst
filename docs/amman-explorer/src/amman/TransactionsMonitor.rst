src/amman/TransactionsMonitor.ts
================================

Last edited: 2022-08-30 20:54:29

Contents:

.. code-block:: ts

    import { LOCALHOST } from "@metaplex-foundation/amman-client";
import { strict as assert } from "assert";
import {
  Connection,
  Context,
  Logs,
  TransactionError,
  TransactionSignature,
} from "@solana/web3.js";
import { AmmanClient, CLEAR_TRANSACTIONS } from "./amman-client";
import { getLatestTransactionSignatures } from "./queries";

export async function transactionHistory() {
  const connection = new Connection(LOCALHOST);
  const currentTransactionSignatures = await getLatestTransactionSignatures();

  const currentTransactionSignaturesWithErrorStatus = await Promise.all(
    currentTransactionSignatures.map(async (x) => {
      const err = await getTransactionError(connection, x.signature);
      return { ...x, err };
    })
  );
  return currentTransactionSignaturesWithErrorStatus;
}

export type TransactionInfo = {
  signature: TransactionSignature;
  block: number;
  index: number;
  err?: TransactionError;
};
export type OnTransactionsChanged = (transactions: TransactionInfo[]) => void;
export class TransactionsMonitor {
  readonly latestTransactions: TransactionInfo[] = [];
  loadedTransactionHistory: boolean;
  transactionCount: number = 0;
  private constructor(
    readonly connection: Connection,
    readonly ammanClient: AmmanClient,
    private onTransactionsChanged: OnTransactionsChanged,
    readonly maxTransactions: number
  ) {
    this.connection.onLogs("all", this.onLog);
    this.ammanClient.on(CLEAR_TRANSACTIONS, this.onClearTransactions);
    this.loadedTransactionHistory = false;
    this.update();
  }

  async loadTransactionHistory() {
    this.latestTransactions.length = 0;
    this.loadedTransactionHistory = true;
    const currentSignatures = await transactionHistory();
    this.addSortedSliceOfSignatures(currentSignatures);
    this.update();
  }

  private addSortedSliceOfSignatures(
    currentSignatures: {
      block: number;
      signature: TransactionSignature;
      err: TransactionError | null | undefined;
    }[]
  ) {
    const sorted = Array.from(currentSignatures).sort(
      ({ block: blockA }, { block: blockB }) => (blockA < blockB ? -1 : 1)
    );
    const len = sorted.length;
    for (const { block, signature, err } of sorted.slice(
      Math.max(len - this.maxTransactions, 0),
      len
    )) {
      this.latestTransactions.push({
        signature,
        block,
        index: ++this.transactionCount,
        err: err ?? undefined,
      });
    }
  }

  private onLog = async (logs: Logs, ctx: Context) => {
    const txsBefore = Array.from(this.latestTransactions);
    const err = (await this.getTransactionError(logs.signature)) ?? undefined;
    this.latestTransactions.push({
      signature: logs.signature,
      block: ctx.slot,
      index: ++this.transactionCount,
      err,
    });
    this._purgeOldSignatures();
    this.update(txsBefore);
  };

  private update(txsBefore: TransactionInfo[] = []) {
    if (
      txsBefore.map((x) => x.signature).join("") !==
      this.latestTransactions.map((x) => x.signature).join("")
    ) {
      const currentTransactions = Array.from(this.latestTransactions).reverse();
      this.onTransactionsChanged(currentTransactions);
    }
  }

  private async getTransactionError(signature: TransactionSignature) {
    const tx = await this.connection.getTransaction(signature, {
      commitment: "confirmed",
    });
    return tx?.meta?.err;
  }

  private _purgeOldSignatures() {
    // Assuming they are sorted by block ascending
    while (this.latestTransactions.length > this.maxTransactions) {
      this.latestTransactions.shift();
    }
  }

  private onClearTransactions = () => {
    this.latestTransactions.length = 0;
    this.transactionCount = 0;
  };

  private static _instance?: TransactionsMonitor;

  static instance(
    url: string,
    ammanClient: AmmanClient,
    onTransactionsChanged: OnTransactionsChanged,
    maxTransactions: number = TransactionsMonitor.DEFAULT_MAX_TRANSACTIONS
  ): TransactionsMonitor {
    if (TransactionsMonitor._instance != null) {
      TransactionsMonitor._instance.onTransactionsChanged =
        onTransactionsChanged;
      return TransactionsMonitor._instance;
    }
    const connection = new Connection(url, "singleGossip");
    TransactionsMonitor._instance = new TransactionsMonitor(
      connection,
      ammanClient,
      onTransactionsChanged,
      maxTransactions
    );
    return TransactionsMonitor._instance;
  }
  static get existingInstance() {
    assert(
      TransactionsMonitor._instance != null,
      "expected existing instance of TransactionsMonitor"
    );
    return TransactionsMonitor._instance;
  }

  static DEFAULT_MAX_TRANSACTIONS = 12;
}

// -----------------
// Helpers
// -----------------

export async function getTransactionError(
  connection: Connection,
  signature: TransactionSignature
) {
  const tx = await connection.getTransaction(signature, {
    commitment: "confirmed",
  });
  return tx?.meta?.err;
}


