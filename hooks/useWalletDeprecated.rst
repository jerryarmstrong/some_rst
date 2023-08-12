hooks/useWalletDeprecated.tsx
=============================

Last edited: 2023-08-11 18:13:34

Contents:

.. code-block:: tsx

    import { AnchorProvider, Wallet } from '@coral-xyz/anchor'
import { useMemo } from 'react'

import useWalletOnePointOh from './useWalletOnePointOh'
import useLegacyConnectionContext from './useLegacyConnectionContext'

/** @deprecated */
export default function useWalletDeprecated() {
  const connection = useLegacyConnectionContext()
  const wallet = useWalletOnePointOh()
  const connected = !!wallet?.connected

  const anchorProvider = useMemo(() => {
    const options = AnchorProvider.defaultOptions()
    return new AnchorProvider(
      connection.current,
      (wallet as unknown) as Wallet,
      options
    )
  }, [connection, wallet])

  return useMemo(() => ({ connected, wallet, anchorProvider, connection }), [
    anchorProvider,
    connected,
    connection,
    wallet,
  ])
}


