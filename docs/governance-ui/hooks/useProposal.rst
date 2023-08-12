hooks/useProposal.tsx
=====================

Last edited: 2023-05-19 22:20:18

Contents:

.. code-block:: tsx

    import { useRouter } from 'next/router'
import useWalletStore from '../stores/useWalletStore'

export default function useProposal() {
  const router = useRouter()
  const { pk } = router.query

  const {
    proposal,
    descriptionLink,
    transactions,
    proposalMint,
    governance,
    proposalOwner,
  } = useWalletStore((s) => s.selectedProposal)

  return {
    pk,
    proposal,
    descriptionLink,
    transactions,
    proposalMint,
    governance,
    proposalOwner,
  }
}


