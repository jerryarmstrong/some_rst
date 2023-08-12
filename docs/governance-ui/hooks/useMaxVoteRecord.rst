hooks/useMaxVoteRecord.ts
=========================

Last edited: 2023-05-19 22:20:18

Contents:

.. code-block:: ts

    import { useMemo } from 'react'
import { MaxVoterWeightRecord, ProgramAccount } from '@solana/spl-governance'
import useNftPluginStore from 'NftVotePlugin/store/nftPluginStore'
import useHeliumVsrStore from 'HeliumVotePlugin/hooks/useHeliumVsrStore'

export const useMaxVoteRecord = () => {
  const nftMaxVoteRecord = useNftPluginStore((s) => s.state.maxVoteRecord)
  const heliumMaxVoteRecord = useHeliumVsrStore((s) => s.state.maxVoteRecord)
  const maxVoteWeightRecord: ProgramAccount<MaxVoterWeightRecord> | null = useMemo(
    () => nftMaxVoteRecord || heliumMaxVoteRecord || null,
    [nftMaxVoteRecord, heliumMaxVoteRecord]
  )

  return maxVoteWeightRecord
}


