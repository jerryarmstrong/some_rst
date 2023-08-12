packages/common/src/hooks/useUserAccounts.ts
============================================

Last edited: 2023-07-19 16:40:40

Contents:

.. code-block:: ts

    import { TokenAccount } from '../models';
import { useAccountsContext } from '../contexts/accounts';

export function useUserAccounts() {
  const context = useAccountsContext();
  return {
    userAccounts: context.userAccounts as TokenAccount[],
  };
}


