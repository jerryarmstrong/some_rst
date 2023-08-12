hub/lib/getDefaultBannerUrl.ts
==============================

Last edited: 2023-05-19 22:20:18

Contents:

.. code-block:: ts

    import type { PublicKey } from '@solana/web3.js';

const NUM_BANNERS = 20;

export function getDefaultBannerUrl(seed: PublicKey | string) {
  const seedStr = typeof seed === 'string' ? seed : seed.toBase58();
  const num = seedStr
    .split('')
    .reduce((acc, cur) => acc + cur.charCodeAt(0), 0);
  const index = (num % NUM_BANNERS) + 1;
  return `/banners/${index}.jpg`;
}


