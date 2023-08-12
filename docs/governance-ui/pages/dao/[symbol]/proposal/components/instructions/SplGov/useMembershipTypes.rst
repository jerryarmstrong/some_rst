pages/dao/[symbol]/proposal/components/instructions/SplGov/useMembershipTypes.ts
================================================================================

Last edited: 2023-05-19 22:20:18

Contents:

.. code-block:: ts

    import useRealm from '@hooks/useRealm'
import { GoverningTokenType } from '@solana/spl-governance'

const useMembershipTypes = () => {
  const { realm, config } = useRealm()
  const maybeCouncil =
    realm?.account.config.councilMint &&
    config?.account.councilTokenConfig.tokenType ===
      GoverningTokenType.Membership
      ? ({ council: realm.account.config.councilMint } as const)
      : ({} as const)
  const maybeCommunity =
    realm?.account.communityMint &&
    config?.account.communityTokenConfig.tokenType ===
      GoverningTokenType.Membership
      ? ({ community: realm.account.communityMint } as const)
      : ({} as const)
  return { ...maybeCouncil, ...maybeCommunity } as const
}
export default useMembershipTypes


