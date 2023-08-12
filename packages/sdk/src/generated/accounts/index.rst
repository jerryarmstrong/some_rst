packages/sdk/src/generated/accounts/index.ts
============================================

Last edited: 2023-06-14 20:00:41

Contents:

.. code-block:: ts

    export * from './CollectionInfo';
export * from './MigrationState';
export * from './MigrationStatus';
export * from './ProgramSigner';

import { MigrationState } from './MigrationState';
import { CollectionInfo } from './CollectionInfo';
import { MigrationStatus } from './MigrationStatus';
import { ProgramSigner } from './ProgramSigner';

export const accountProviders = { MigrationState, CollectionInfo, MigrationStatus, ProgramSigner };


