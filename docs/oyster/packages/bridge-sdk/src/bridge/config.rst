packages/bridge-sdk/src/bridge/config.ts
========================================

Last edited: 2023-07-19 16:40:40

Contents:

.. code-block:: ts

    // 44 - bridge config
import { publicKey } from '@oyster/common/dist/lib/utils/layout';
import * as BufferLayout from 'buffer-layout';

export const BridgeLayout = BufferLayout.struct([
  BufferLayout.u32('guardianSetIndex'),
  BufferLayout.u8('guardianSetExpirationTime'),
  publicKey('tokenProgram'),
  BufferLayout.u8('isInitialized'),
]);


