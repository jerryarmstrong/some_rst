pages/dao/[symbol]/proposal/components/MinimumApprovalThreshold.tsx
===================================================================

Last edited: 2023-05-19 22:20:18

Contents:

.. code-block:: tsx

    import ProgressBar from '@components/ProgressBar'

import { Governance } from '@solana/spl-governance'
import { ProgramAccount } from '@solana/spl-governance'
import React from 'react'

const MinimumApprovalThreshold = ({
  governance,
}: {
  governance: ProgramAccount<Governance> | null
}) => {
  const info = governance?.account
  // const info = { config: { voteThresholdPercentage: { value: 50 } } }
  return info ? (
    <ProgressBar
      progress={info?.config.communityVoteThreshold.value}
      prefix="Approval quorum"
    ></ProgressBar>
  ) : null
}

export default MinimumApprovalThreshold


