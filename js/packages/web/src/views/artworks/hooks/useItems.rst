js/packages/web/src/views/artworks/hooks/useItems.ts
====================================================

Last edited: 2022-06-29 06:18:54

Contents:

.. code-block:: ts

    import { useMeta } from '@oyster/common';
import { useWallet } from '@solana/wallet-adapter-react';

import { useCreatorArts } from '../../../hooks';
import { ArtworkViewState, Item } from '../types';

import { useUserMetadataWithPacks } from './useUserMetadataWithPacks';
import { usePacksBasedOnProvingProcesses } from './usePacksBasedOnProvingProcesses';

export const useItems = ({
  activeKey,
}: {
  activeKey: ArtworkViewState;
}): Item[] => {
  const { publicKey } = useWallet();
  const { metadata } = useMeta();
  const createdMetadata = useCreatorArts(publicKey?.toBase58() || '');
  const userMetadataWithPacks = useUserMetadataWithPacks();
  const packsBasedOnProvingProcesses = usePacksBasedOnProvingProcesses();

  if (activeKey === ArtworkViewState.Owned) {
    return [...userMetadataWithPacks, ...packsBasedOnProvingProcesses];
  }

  if (activeKey === ArtworkViewState.Created) {
    return createdMetadata;
  }

  return metadata;
};


