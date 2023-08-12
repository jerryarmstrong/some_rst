src/actions/candy-machine/create.ts
===================================

Last edited: 2022-10-10 15:06:28

Contents:

.. code-block:: ts

    import {
  CreateCandyMachineInput,
  Metaplex,
  NftWithToken,
} from '@metaplex-foundation/js'
import { CandyMachineCreateArgs } from '@/types'
import { strict as assert } from 'assert'
import { tryAmman } from '@/utils/amman'
import { ConfirmOptions } from '@solana/web3.js'

export async function candyMachineCreate(
  mx: Metaplex,
  args: CandyMachineCreateArgs
) {
  const nft =
    args.collection ??
    (await createCollection(
      mx,
      'MyCollectionNft',
      'http://some/uri',
      100,
      args.confirmOptions
    ))
  const collection = {
    address: nft.address,
    updateAuthority: mx.identity(),
  }
  const input: CreateCandyMachineInput = { ...args, collection }
  const { response, candyMachine, candyMachineSigner } = await mx
    .candyMachines()
    .create(input)
    .run()

  const amman = tryAmman()
  if (amman != null) {
    await amman.addr.addLabel('tx: create candy machine', response.signature)
    await amman.addr.addLabels(candyMachine)
    await amman.addr.addLabels(candyMachine.candyGuard)
    await amman.addr.addLabels(candyMachine.creators)
    await amman.addr.addLabel(
      'candyMachineSigner',
      candyMachineSigner.publicKey
    )
  }
  return candyMachine
}

// TODO(thlorenz): This is a stop gap ... we need to have the user create a collection first via
// mplex nft create ... and then provide us the address
async function createCollection(
  mx: Metaplex,
  collectionName: string,
  uri: string,
  sellerFeeBasisPoints: number,
  confirmOptions?: ConfirmOptions
): Promise<NftWithToken> {
  const { nft, response, ...rest } = await mx
    .nfts()
    .create({
      isCollection: true,
      name: collectionName,
      uri,
      sellerFeeBasisPoints,
      confirmOptions,
    })
    .run()

  const amman = tryAmman()
  if (amman != null) {
    await amman.addr.addLabel('tx: create collection', response.signature)
    await amman.addr.addLabels(nft)
    await amman.addr.addLabels(nft.mint)
    await amman.addr.addLabels(rest)
  }

  assert(
    nft.address != null,
    'Should have created an NFT with collection address'
  )
  return nft
}


