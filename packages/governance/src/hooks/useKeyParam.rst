packages/governance/src/hooks/useKeyParam.ts
============================================

Last edited: 2023-07-19 16:40:40

Contents:

.. code-block:: ts

    import { PublicKey } from '@solana/web3.js';
import { useParams } from 'react-router-dom';

export const useKeyParam = () => {
  const { key } = useParams<{ key: string }>();
  return new PublicKey(key);
};


