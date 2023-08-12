packages/lending/src/hooks/useUserDeposits.ts
=============================================

Last edited: 2023-07-19 16:40:40

Contents:

.. code-block:: ts

    import { calculateDepositAPY, LendingReserve } from '../models/lending';
import { useLendingReserves } from './useLendingReserves';
import { useEffect, useMemo, useState } from 'react';
import { useMarkets } from '../contexts/market';
import { calculateCollateralBalance } from './useCollateralBalance';
import { MintInfo } from '@solana/spl-token';

import {
  contexts,
  utils,
  ParsedAccount,
  TokenAccount,
  hooks,
} from '@oyster/common';
const { cache } = contexts.Accounts;
const { useConnectionConfig } = contexts.Connection;
const { fromLamports, getTokenName } = utils;
const { useUserAccounts } = hooks;

export interface UserDeposit {
  account: TokenAccount;
  info: {
    amount: number;
    amountInQuote: number;
    apy: number;
    name: string;
    precision: number;
  };
  reserve: ParsedAccount<LendingReserve>;
}

export function useUserDeposits(exclude?: Set<string>, include?: Set<string>) {
  const { userAccounts } = useUserAccounts();
  const { reserveAccounts } = useLendingReserves();
  const [userDeposits, setUserDeposits] = useState<UserDeposit[]>([]);
  const { marketEmitter, midPriceInUSD } = useMarkets();
  const { tokenMap } = useConnectionConfig();

  const reservesByCollateralMint = useMemo(() => {
    return reserveAccounts.reduce((result, item) => {
      const id = item.pubkey.toBase58();
      if (exclude && exclude.has(id)) {
        return result;
      }

      if (!include || include.has(id)) {
        result.set(item.info.collateralMint.toBase58(), item);
      }

      return result;
    }, new Map<string, ParsedAccount<LendingReserve>>());
  }, [reserveAccounts, exclude, include]);

  useEffect(() => {
    const activeMarkets = new Set(
      reserveAccounts.map(r => r.info.dexMarket.toBase58()),
    );

    const userDepositsFactory = () => {
      return userAccounts
        .filter(acc => reservesByCollateralMint.has(acc?.info.mint.toBase58()))
        .map(item => {
          const reserve = reservesByCollateralMint.get(
            item?.info.mint.toBase58(),
          ) as ParsedAccount<LendingReserve>;

          let collateralMint = cache.get(
            reserve.info.collateralMint,
          ) as ParsedAccount<MintInfo>;

          const amountLamports = calculateCollateralBalance(
            reserve.info,
            item?.info.amount.toNumber(),
          );
          const amount = fromLamports(amountLamports, collateralMint?.info);
          const price = midPriceInUSD(reserve.info.liquidityMint.toBase58());
          const amountInQuote = price * amount;

          return {
            account: item,
            info: {
              amount,
              amountInQuote: amountInQuote,
              apy: calculateDepositAPY(reserve.info),
              name: getTokenName(tokenMap, reserve.info.liquidityMint),
            },
            reserve,
          } as UserDeposit;
        })
        .sort((a, b) => b.info.amountInQuote - a.info.amountInQuote);
    };

    const dispose = marketEmitter.onMarket(args => {
      // ignore if none of the markets is used by the reserve
      if ([...args.ids.values()].every(id => !activeMarkets.has(id))) {
        return;
      }

      setUserDeposits(userDepositsFactory());
    });

    setUserDeposits(userDepositsFactory());

    return () => {
      dispose();
    };
  }, [
    userAccounts,
    reserveAccounts,
    reservesByCollateralMint,
    tokenMap,
    midPriceInUSD,
    marketEmitter,
  ]);

  return {
    userDeposits,
    totalInQuote: userDeposits.reduce(
      (res, item) => res + item.info.amountInQuote,
      0,
    ),
  };
}


