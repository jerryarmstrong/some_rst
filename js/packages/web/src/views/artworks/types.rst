js/packages/web/src/views/artworks/types.ts
===========================================

Last edited: 2022-06-29 06:18:54

Contents:

.. code-block:: ts

    import { Metadata, ParsedAccount } from '@oyster/common';
import { SafetyDepositDraft } from '../../actions/createAuctionManager';
import { ExtendedPack } from '../../types/packs';

export type Item = ExtendedPack | SafetyDepositDraft | ParsedAccount<Metadata>;

export enum ArtworkViewState {
  Metaplex = '0',
  Owned = '1',
  Created = '2',
}


