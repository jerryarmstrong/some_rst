js/packages/web/src/views/artworks/utils.ts
===========================================

Last edited: 2022-06-29 06:18:54

Contents:

.. code-block:: ts

    import { Metadata, ParsedAccount } from '@oyster/common';
import { ExtendedPack } from '../../types/packs';
import { Item } from './types';

export const isPack = (item: Item): item is ExtendedPack =>
  (item as ExtendedPack)?.info && !!(item as ExtendedPack).info.randomOracle;

export const isMetadata = (item: Item): item is ParsedAccount<Metadata> =>
  (item as ParsedAccount<Metadata>)?.info &&
  !!(item as ParsedAccount<Metadata>).info.data;


