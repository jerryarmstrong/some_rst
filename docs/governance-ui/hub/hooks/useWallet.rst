hub/hooks/useWallet.ts
======================

Last edited: 2023-05-19 22:20:18

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


