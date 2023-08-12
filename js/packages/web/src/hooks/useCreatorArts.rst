js/packages/web/src/hooks/useCreatorArts.ts
===========================================

Last edited: 2022-06-29 06:18:54

Contents:

.. code-block:: ts

    import { useMeta } from '../contexts';
import { StringPublicKey } from '@oyster/common';

export const useCreatorArts = (id?: StringPublicKey) => {
  const { metadata } = useMeta();
  const filtered = metadata.filter(m =>
    m.info.data.creators?.some(c => c.address === id),
  );

  return filtered;
};


