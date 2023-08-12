packages/js/src/plugins/storageModule/StorageDriver.ts
======================================================

Last edited: 2023-05-26 09:49:40

Contents:

.. code-block:: ts

    import { RequestInit } from 'node-fetch';
import { MetaplexFile } from './MetaplexFile';
import { Amount } from '@/types';

export type StorageDriver = {
  getUploadPrice: (bytes: number) => Promise<Amount>;
  upload: (file: MetaplexFile) => Promise<string>;
  uploadAll?: (files: MetaplexFile[]) => Promise<string[]>;
  download?: (
    uri: string,
    options?: StorageDownloadOptions
  ) => Promise<MetaplexFile>;
  getUploadPriceForFiles?: (files: MetaplexFile[]) => Promise<Amount>;
};

export type StorageDownloadOptions = Omit<RequestInit, 'signal'> & {
  signal?: AbortSignal | null;
};


