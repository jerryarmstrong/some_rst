amman/src/amman.ts
==================

Last edited: 2022-11-03 12:19:53

Contents:

.. code-block:: ts

    import * as AmmanClient from '@metaplex-foundation/amman-client'

export { tmpLedgerDir } from './utils'
export { Change } from './accounts/state'
export * from './types'

// -----------------
// Forwarding some amman-client exports
// -----------------
export {
  AmmanAccountRendererMap,
  LOCALHOST,
} from '@metaplex-foundation/amman-client'

/**
 * @deprecated Use from _amman-client_ directly via `import { Amman } from '@metaplex-foundation/amman-client'`
 */
export const Amman = AmmanClient.Amman


