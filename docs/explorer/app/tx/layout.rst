app/tx/layout.tsx
=================

Last edited: 2023-07-31 09:08:44

Contents:

.. code-block:: tsx

    import { TransactionsProvider } from '@providers/transactions';
import { PropsWithChildren } from 'react';

import { AccountsProvider } from '../providers/accounts';

export default function TxLayout({ children }: PropsWithChildren<Record<string, never>>) {
  return (
    <TransactionsProvider>
      <AccountsProvider>
        {children}
      </AccountsProvider>
    </TransactionsProvider>
  );
}


