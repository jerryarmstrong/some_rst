src/wallet-adapters/sollet-extension/index.tsx
==============================================

Last edited: 2021-05-21 14:15:46

Contents:

.. code-block:: tsx

    import Wallet from '@project-serum/sol-wallet-adapter';
import { notify } from '../../utils/notifications';

export function SolletExtensionAdapter(_, network) {
  const sollet = (window as any).sollet;
  if (sollet) {
    return new Wallet(sollet, network);
  }

  return {
    on: () => {},
    connect: () => {
      notify({
        message: 'Sollet Extension Error',
        description: 'Please install the Sollet Extension for Chrome',
      });
    }
  }
}

