src/gateway/client.ts
=====================

Last edited: 2023-06-01 19:30:16

Contents:

.. code-block:: ts

    import { Program, Provider } from '@project-serum/anchor';
import { PublicKey } from '@solana/web3.js';
import { Gateway, IDL } from './gateway';

export const GATEWAY_PLUGIN_ID = new PublicKey(
  'GgathUhdrCWRHowoRKACjgWhYHfxCEdBi5ViqYN6HVxk'
);

export class GatewayClient {
  constructor(public program: Program<Gateway>, public devnet?: boolean) {}

  static async connect(
    provider: Provider,
    devnet?: boolean,
  ): Promise<GatewayClient> {
    // alternatively we could fetch from chain
    // const idl = await Program.fetchIdl(GATEWAY_PLUGIN_ID, provider);
    const idl = IDL;

    return new GatewayClient(
      new Program<Gateway>(idl as Gateway, GATEWAY_PLUGIN_ID, provider),
      devnet,
    );
  }
}


