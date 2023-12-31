hooks/queries/addresses/voteRecord.ts
=====================================

Last edited: 2023-05-19 22:20:18

Contents:

.. code-block:: ts

    import useRealm from '@hooks/useRealm'
import { getVoteRecordAddress } from '@solana/spl-governance'
import { PublicKey } from '@solana/web3.js'
import { useQuery } from '@tanstack/react-query'
import { useRouter } from 'next/router'

export const useAddressQuery_SelectedProposalVoteRecord = (
  tokenOwnerRecordAddress?: PublicKey
) => {
  const router = useRouter()
  const { pk } = router.query
  const { realm } = useRealm()

  const programId = realm?.owner // TODO make me cached plz
  const proposalAddress = typeof pk === 'string' ? new PublicKey(pk) : undefined

  return useAddressQuery_VoteRecord(
    programId,
    proposalAddress,
    tokenOwnerRecordAddress
  )
}

export const useAddressQuery_VoteRecord = (
  programId?: PublicKey,
  proposalAddress?: PublicKey,
  tokenOwnerRecordAddress?: PublicKey
) => {
  const enabled =
    programId !== undefined &&
    proposalAddress !== undefined &&
    tokenOwnerRecordAddress !== undefined

  return useQuery({
    queryKey: enabled
      ? [
          'VoteRecordAddress',
          [programId, proposalAddress, tokenOwnerRecordAddress],
        ]
      : undefined,
    queryFn: () => {
      if (!enabled) throw new Error()

      return getVoteRecordAddress(
        programId,
        proposalAddress,
        tokenOwnerRecordAddress
      )
    },
    enabled,
    // Staletime is zero by default, so queries get refetched often. PDAs will never go stale.
    staleTime: Number.MAX_SAFE_INTEGER,
  })
}


