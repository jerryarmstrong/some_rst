js/packages/web/src/views/pack/contexts/utils/getMetadataUserToReceive.ts
=========================================================================

Last edited: 2022-06-29 06:18:54

Contents:

.. code-block:: ts

    import {
  findPackCardProgramAddress,
  StringPublicKey,
  toPublicKey,
} from '@oyster/common';
import { PackMetadataByPackCard } from '../hooks/useMetadataByPackCard';

interface GetMetadataUserToReceiveParams {
  cardsToRedeem: Map<number, number>;
  metadataByPackCard: PackMetadataByPackCard;
  packPubKey: StringPublicKey;
}

// Returns metadata that user should receive as a result of pack opening
export const getMetadataUserToReceive = async ({
  cardsToRedeem,
  metadataByPackCard,
  packPubKey,
}: GetMetadataUserToReceiveParams): Promise<StringPublicKey[]> => {
  const metadataUserToReceive: StringPublicKey[] = [];
  for (const [index, numberToRedeem] of cardsToRedeem.entries()) {
    const packCard = await findPackCardProgramAddress(
      toPublicKey(packPubKey),
      index,
    );
    const metadataByCard = metadataByPackCard[packCard];

    for (let i = 0; i < numberToRedeem; i++) {
      metadataUserToReceive.push(metadataByCard.pubkey);
    }
  }

  return metadataUserToReceive;
};


