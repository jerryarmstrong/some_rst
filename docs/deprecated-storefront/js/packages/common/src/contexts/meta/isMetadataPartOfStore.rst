js/packages/common/src/contexts/meta/isMetadataPartOfStore.ts
=============================================================

Last edited: 2022-06-29 06:18:54

Contents:

.. code-block:: ts

    import { Metadata } from '../../actions';
import { Store, WhitelistedCreator } from '../../models/metaplex';
import { ParsedAccount } from '../accounts/types';

export const isMetadataPartOfStore = (
  m: ParsedAccount<Metadata>,
  whitelistedCreatorsByCreator: Record<
    string,
    ParsedAccount<WhitelistedCreator>
  >,
  store?: ParsedAccount<Store> | null,
) => {
  if (!m?.info?.data?.creators) {
    return false;
  }

  return m.info.data.creators.some(
    c =>
      c.verified &&
      (store?.info.public ||
        whitelistedCreatorsByCreator[c.address]?.info?.activated),
  );
};


