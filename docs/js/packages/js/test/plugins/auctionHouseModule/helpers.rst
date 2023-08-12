packages/js/test/plugins/auctionHouseModule/helpers.ts
======================================================

Last edited: 2023-05-26 09:49:40

Contents:

.. code-block:: ts

    import type { Metaplex } from '@/Metaplex';
import { CreateAuctionHouseInput } from '@/plugins';
import { sol, Signer, OperationOptions } from '@/types';

export const createAuctionHouse = async (
  mx: Metaplex,
  auctioneerAuthority?: Signer | null,
  input: Partial<CreateAuctionHouseInput> = {},
  options: OperationOptions = {}
) => {
  const { auctionHouse } = await mx.auctionHouse().create(
    {
      sellerFeeBasisPoints: 200,
      auctioneerAuthority: auctioneerAuthority?.publicKey,
      ...input,
    },
    options
  );

  await mx.rpc().airdrop(auctionHouse.feeAccountAddress, sol(100));

  return auctionHouse;
};


