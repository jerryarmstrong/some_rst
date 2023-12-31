packages/bridge/src/hooks/useCorrectNetwork.tsx
===============================================

Last edited: 2023-07-19 16:40:40

Contents:

.. code-block:: tsx

    import { useEthereum } from '../contexts';
import { useEffect, useState } from 'react';
import { useConnectionConfig } from '@oyster/common';

export const useCorrectNetwork = () => {
  const { env } = useConnectionConfig();
  const [hasCorrespondingNetworks, setHasCorrespondingNetworks] = useState(
    true,
  );
  const { connected, chainId } = useEthereum();

  useEffect(() => {
    if (connected) {
      if (chainId === 5) {
        setHasCorrespondingNetworks(env === 'testnet');
      } else if (chainId === 1) {
        setHasCorrespondingNetworks(env.includes('mainnet-beta'));
      } else {
        setHasCorrespondingNetworks(false);
      }
    } else {
      setHasCorrespondingNetworks(true);
    }
  }, [connected, env, chainId]);

  return { hasCorrespondingNetworks };
};


