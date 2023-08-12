ui/src/lib/UserAccount.tsx
==========================

Last edited: 2023-08-09 02:22:59

Contents:

.. code-block:: tsx

    import { TokenE } from "@/lib/Token";

export class UserAccount {
  public lpBalances: Record<string, number>;
  public tokenBalances: Record<TokenE, number>;

  constructor(
    lpBalances: Record<string, number> = {},
    tokenBalances: Record<string, number> = {}
  ) {
    this.lpBalances = lpBalances;
    this.tokenBalances = tokenBalances;
  }

  getUserLpBalance(poolAddress: string): number {
    return this.lpBalances[poolAddress] || 0;
  }
}


