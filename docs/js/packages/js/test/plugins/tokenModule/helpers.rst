packages/js/test/plugins/tokenModule/helpers.ts
===============================================

Last edited: 2023-05-26 09:49:40

Contents:

.. code-block:: ts

    import { Test } from 'tape';
import {
  formatAmount,
  isEqualToAmount,
  SplTokenAmount,
  Token,
  TokenWithMint,
} from '@/index';
import type { Metaplex } from '@/Metaplex';

export const assertTokenHasAmount = (
  t: Test,
  token: Token | TokenWithMint,
  amount: SplTokenAmount
) => {
  t.true(
    isEqualToAmount(token.amount, amount),
    `token has amount: ${formatAmount(amount)}`
  );
};

export const assertRefreshedTokenHasAmount = async (
  t: Test,
  metaplex: Metaplex,
  token: Token | TokenWithMint,
  amount: SplTokenAmount
) => {
  const refreshedToken = await refreshToken(metaplex, token);
  assertTokenHasAmount(t, refreshedToken, amount);
};

export const refreshToken = (
  metaplex: Metaplex,
  token: Token | TokenWithMint
) => {
  return metaplex.tokens().findTokenByAddress({ address: token.address });
};


