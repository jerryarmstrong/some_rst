GatewayPlugin/sdk/api.ts
========================

Last edited: 2023-05-19 22:20:18

Contents:

.. code-block:: ts

    import { PublicKey } from '@solana/web3.js'
import { GatewayClient } from '@solana/governance-program-library'

export const tryGetGatewayRegistrar = async (
  registrarPk: PublicKey,
  client: GatewayClient
) => {
  try {
    const existingRegistrar = await client.program.account.registrar.fetch(
      registrarPk
    )
    return existingRegistrar
  } catch (e) {
    return null
  }
}


