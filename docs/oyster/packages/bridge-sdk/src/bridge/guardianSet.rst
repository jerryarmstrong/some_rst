packages/bridge-sdk/src/bridge/guardianSet.ts
=============================================

Last edited: 2023-07-19 16:40:40

Contents:

.. code-block:: ts

    import * as BufferLayout from 'buffer-layout';

// 420
export const GuardianSetLayout: typeof BufferLayout.Structure = BufferLayout.struct(
  [
    BufferLayout.u32('index'),
    BufferLayout.u8('keysLength'),

    // TODO: decode keys
    BufferLayout.blob(406, 'keys'),

    BufferLayout.u32('creationTime'),
    BufferLayout.u32('expirationTime'),
    BufferLayout.u8('isInitialized'),
  ],
);


