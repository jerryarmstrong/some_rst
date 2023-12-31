components/treasuryV2/WalletList/NewWalletButton.tsx
====================================================

Last edited: 2023-05-19 22:20:18

Contents:

.. code-block:: tsx

    import { PlusCircleIcon } from '@heroicons/react/outline'
import { useRouter } from 'next/router'
import useRealm from '@hooks/useRealm'
import Tooltip from '@components/Tooltip'
import { LinkButton } from '@components/Button'
import useQueryContext from '@hooks/useQueryContext'
import useWalletOnePointOh from '@hooks/useWalletOnePointOh'

export const NEW_TREASURY_ROUTE = `/treasury/new`

export default function NewWalletButton() {
  const wallet = useWalletOnePointOh()
  const connected = !!wallet?.connected
  const {
    ownVoterWeight,
    realm,
    symbol,
    toManyCommunityOutstandingProposalsForUser,
    toManyCouncilOutstandingProposalsForUse,
  } = useRealm()
  const router = useRouter()
  const { fmtUrlWithCluster } = useQueryContext()

  const canCreateGovernance = !!(realm
    ? ownVoterWeight.canCreateGovernance(realm)
    : null)

  const addNewAssetTooltip = !connected
    ? 'Connect your wallet to create new asset'
    : !canCreateGovernance
    ? "You don't have enough governance power to create a new asset"
    : toManyCommunityOutstandingProposalsForUser
    ? 'You have too many community outstanding proposals. You need to finalize them before creating a new asset.'
    : toManyCouncilOutstandingProposalsForUse
    ? 'You have too many council outstanding proposals. You need to finalize them before creating a new asset.'
    : ''

  const isConnectedWithGovernanceCreationPermission =
    connected &&
    canCreateGovernance &&
    !toManyCommunityOutstandingProposalsForUser &&
    !toManyCouncilOutstandingProposalsForUse

  return (
    <Tooltip contentClassName="ml-auto" content={addNewAssetTooltip}>
      <LinkButton
        className="flex items-center text-primary-light whitespace-nowrap"
        disabled={!isConnectedWithGovernanceCreationPermission}
        onClick={() =>
          router.push(fmtUrlWithCluster(`/dao/${symbol}${NEW_TREASURY_ROUTE}`))
        }
      >
        <PlusCircleIcon className="w-5 h-5 mr-2" />
        New DAO wallet
      </LinkButton>
    </Tooltip>
  )
}


