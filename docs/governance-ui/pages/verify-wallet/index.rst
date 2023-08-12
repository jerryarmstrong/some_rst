pages/verify-wallet/index.tsx
=============================

Last edited: 2023-05-19 22:20:18

Contents:

.. code-block:: tsx

    import VerifyWallet from '@verify-wallet/components'
import { Application } from '@verify-wallet/constants'

export default () => {
  const parsedLocationHash = new URLSearchParams(
    window.location.search.substring(1)
  )

  return (
    <VerifyWallet
      application={Application.SOLANA}
      discordCode={parsedLocationHash.get('code')}
    />
  )
}


