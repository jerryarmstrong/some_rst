js/packages/web/src/hooks/useCreator.ts
=======================================

Last edited: 2022-06-29 06:18:54

Contents:

.. code-block:: ts

    import { StringPublicKey, pubkeyToString } from '@oyster/common';
import { useMeta } from '../contexts';

export const useCreator = (id?: StringPublicKey) => {
  const { whitelistedCreatorsByCreator } = useMeta();
  const key = pubkeyToString(id);
  const creator = Object.values(whitelistedCreatorsByCreator).find(
    creator => creator.info.address === key,
  );
  return creator;
};


