src/hooks/useUserAccounts.ts
============================

Last edited: 2021-03-16 20:45:52

Contents:

.. code-block:: ts

    import { TokenAccount } from "../models";
import { useAccountsContext } from "./../contexts/accounts";

export function useUserAccounts() {
  const context = useAccountsContext();
  return {
    userAccounts: context.userAccounts as TokenAccount[],
  };
}


