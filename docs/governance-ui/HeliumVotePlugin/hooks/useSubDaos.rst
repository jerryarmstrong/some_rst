HeliumVotePlugin/hooks/useSubDaos.ts
====================================

Last edited: 2023-05-19 22:20:18

Contents:

.. code-block:: ts

    import useWalletDeprecated from '@hooks/useWalletDeprecated'
import { web3 } from '@coral-xyz/anchor'
import { useAsync, UseAsyncReturn } from 'react-async-hook'
import { SubDaoWithMeta } from '../sdk/types'
import { PROGRAM_ID } from '@helium/helium-sub-daos-sdk'
import { getSubDaos } from '../utils/getSubDaos'

export const useSubDaos = (
  programId: web3.PublicKey = PROGRAM_ID
): UseAsyncReturn<SubDaoWithMeta[]> => {
  const {
    connection: { current },
    anchorProvider: provider,
  } = useWalletDeprecated()
  return useAsync(getSubDaos, [current, provider, programId])
}


