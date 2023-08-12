src/providers/storage/Storage.ts
================================

Last edited: 2022-06-14 09:19:26

Contents:

.. code-block:: ts

    import { Buffer } from 'buffer';

export interface UploadResult {
  error?: string;
}

export abstract class Storage {
  getAssetCostToStore: (
    files: Map<string, Buffer>,
    arweaveRate: number,
    solanaRate: number,
  ) => Promise<number>;
  upload: (files: Map<string, Buffer>, mintKey: string, txid: string) => Promise<UploadResult>;
}


