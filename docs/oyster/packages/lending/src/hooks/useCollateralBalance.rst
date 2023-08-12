packages/lending/src/hooks/useCollateralBalance.ts
==================================================

Last edited: 2023-07-19 16:40:40

Contents:

.. code-block:: ts

    import { PublicKey } from '@solana/web3.js';
import { useEffect, useMemo, useState } from 'react';
import { useMarkets } from '../contexts/market';
import { LendingReserve, reserveMarketCap } from '../models/lending';
import { useUserBalance } from './useUserBalance';

import { contexts, utils } from '@oyster/common';
const { useMint } = contexts.Accounts;
const { fromLamports } = utils;

export function useUserCollateralBalance(
  reserve?: LendingReserve,
  account?: PublicKey,
) {
  const mint = useMint(reserve?.collateralMint);
  const { balanceLamports: userBalance, accounts } = useUserBalance(
    reserve?.collateralMint,
    account,
  );

  const [balanceInUSD, setBalanceInUSD] = useState(0);
  const { marketEmitter, midPriceInUSD } = useMarkets();

  const balanceLamports = useMemo(
    () => reserve && calculateCollateralBalance(reserve, userBalance),
    [userBalance, reserve],
  );

  const balance = useMemo(() => fromLamports(balanceLamports, mint), [
    balanceLamports,
    mint,
  ]);

  useEffect(() => {
    const updateBalance = () => {
      setBalanceInUSD(
        balance * midPriceInUSD(reserve?.liquidityMint?.toBase58() || ''),
      );
    };

    const dispose = marketEmitter.onMarket(args => {
      if (args.ids.has(reserve?.dexMarket.toBase58() || '')) {
        updateBalance();
      }
    });

    updateBalance();

    return () => {
      dispose();
    };
  }, [balance, midPriceInUSD, marketEmitter, mint, setBalanceInUSD, reserve]);

  return {
    balance,
    balanceLamports,
    balanceInUSD,
    mint: reserve?.collateralMint,
    accounts,
    hasBalance: accounts.length > 0 && balance > 0,
  };
}
export function calculateCollateralBalance(
  reserve: LendingReserve,
  balanceLamports: number,
) {
  return (
    reserveMarketCap(reserve) *
    (balanceLamports / (reserve?.state.collateralMintSupply.toNumber() || 1))
  );
}


