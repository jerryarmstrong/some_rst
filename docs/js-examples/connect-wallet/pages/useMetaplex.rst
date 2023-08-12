connect-wallet/pages/useMetaplex.js
===================================

Last edited: 2023-05-10 12:33:36

Contents:

.. code-block:: js

    import { createContext, useContext } from 'react';

const DEFAULT_CONTEXT = {
  metaplex: null,
};

export const MetaplexContext = createContext(DEFAULT_CONTEXT);

export function useMetaplex() {
  return useContext(MetaplexContext);
}


