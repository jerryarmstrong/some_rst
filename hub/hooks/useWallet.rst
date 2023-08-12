hub/hooks/useWallet.ts
======================

Last edited: 2023-08-11 18:13:34

Contents:

.. code-block:: ts

    import { useContext } from 'react';

import { context } from '@hub/providers/Wallet';

export function useWallet() {
  const {
    connect,
    publicKey,
    softConnect,
    setSoftConnect,
    signMessage,
    signTransaction,
    signAllTransactions,
  } = useContext(context);
  return {
    connect,
    publicKey,
    softConnect,
    setSoftConnect,
    signMessage,
    signTransaction,
    signAllTransactions,
  };
}


