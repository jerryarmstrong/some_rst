packages/lending/src/hooks/useLendingMarket.ts
==============================================

Last edited: 2023-07-19 16:40:40

Contents:

.. code-block:: ts

    import { contexts, ParsedAccount } from '@oyster/common';
import { PublicKey } from '@solana/web3.js';
import { useEffect, useState } from 'react';
import { LendingMarketParser, LendingMarket } from '../models/lending';
const { cache } = contexts.Accounts;

const getLendingMarkets = () => {
  return cache
    .byParser(LendingMarketParser)
    .map(id => cache.get(id))
    .filter(acc => acc !== undefined) as any[];
};

export function useLendingMarkets() {
  const [lendingMarkets, setLendingMarket] = useState<
    ParsedAccount<LendingMarket>[]
  >(getLendingMarkets());

  useEffect(() => {
    const dispose = cache.emitter.onCache(args => {
      if (args.parser === LendingMarketParser) {
        setLendingMarket(getLendingMarkets());
      }
    });

    return () => {
      dispose();
    };
  }, [setLendingMarket]);

  return {
    lendingMarkets,
  };
}

export function useLendingMarket(address?: string | PublicKey) {
  const id = typeof address === 'string' ? address : address?.toBase58();
  const [lendingMarket, setLendingMarket] = useState<
    ParsedAccount<LendingMarket>
  >(cache.get(id || '') as ParsedAccount<LendingMarket>);

  useEffect(() => {
    const dispose = cache.emitter.onCache(args => {
      if (args.id === id) {
        setLendingMarket(cache.get(id) as ParsedAccount<LendingMarket>);
      }
    });

    return () => {
      dispose();
    };
  }, [id, setLendingMarket]);

  return lendingMarket;
}


