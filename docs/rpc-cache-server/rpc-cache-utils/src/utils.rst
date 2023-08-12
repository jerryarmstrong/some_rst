rpc-cache-utils/src/utils.ts
============================

Last edited: 2021-08-05 17:33:45

Contents:

.. code-block:: ts

    export interface ParsedKeyedAccountInfo {
  pubkey: string;
  account: {
    executable: boolean;
    lamports: number;
    rentEpoch: number;
    owner: string;
    data: any;
  };
}

export function sleep(ms: number): Promise<void> {
  return new Promise((resolve) => setTimeout(resolve, ms));
}


