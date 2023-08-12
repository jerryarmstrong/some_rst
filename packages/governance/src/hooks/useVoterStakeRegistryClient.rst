packages/governance/src/hooks/useVoterStakeRegistryClient.ts
============================================================

Last edited: 2023-07-19 16:40:40

Contents:

.. code-block:: ts

    import { useConnectionConfig, useConnection, useWallet } from '@oyster/common';
import { useEffect, useState } from 'react';

import { useProgramInfo } from '../contexts/GovernanceContext';
import { Provider, Wallet } from '@project-serum/anchor';
import { VsrClient } from '@blockworks-foundation/voter-stake-registry-client';

export function useVoterStakeRegistryClient() {
  const { endpoint, env } = useConnectionConfig();
  const connection = useConnection();
  const wallet = useWallet();
  const { programId, programVersion } = useProgramInfo();
  const [client, setClient] = useState<VsrClient>();

  useEffect(
    () => {
      const handleSetClient = async () => {
        const options = Provider.defaultOptions();
        const provider = new Provider(
          connection,
          (wallet as unknown) as Wallet,
          options,
        );
        const vsrClient = await VsrClient.connect(provider, env === 'devnet');
        setClient(vsrClient);
      };
      if (wallet.connected) {
        handleSetClient();
      }
    },
    // eslint-disable-next-line react-hooks/exhaustive-deps
    [programId, connection, wallet, endpoint, programVersion],
  );

  return client;
}


