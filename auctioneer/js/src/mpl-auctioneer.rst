auctioneer/js/src/mpl-auctioneer.ts
===================================

Last edited: 2023-07-31 23:00:16

Contents:

.. code-block:: ts

    import { PROGRAM_ADDRESS, PROGRAM_ID } from './generated';

export * from './generated';
export * from './errors';
// Used by Amman to resolve account data
export * as accountProviders from './generated/accounts';

export const AUCTIONEER_PREFIX = 'auctioneer';
export const AUCTIONEER_PROGRAM_ADDRESS = PROGRAM_ADDRESS;
export const AUCTIONEER_PROGRAM_ID = PROGRAM_ID;


