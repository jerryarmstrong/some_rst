hub/lib/gqlCacheStorage.ts
==========================

Last edited: 2023-08-11 18:13:34

Contents:

.. code-block:: ts

    import * as localforage from 'localforage';

export const getName = (jwt: string | null) => {
  if (!jwt) {
    return 'realms-anon';
  }

  return `realms-${jwt}`;
};

export const create = (jwt: string | null) => {
  const name = getName(jwt);
  return localforage.createInstance({ name });
};

export const destroy = (jwt: string | null) => {
  const name = getName(jwt);
  return localforage.dropInstance({ name });
};


