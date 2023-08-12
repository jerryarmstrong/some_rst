hooks/useUserOrDelegator.ts
===========================

Last edited: 2023-08-11 18:13:34

Contents:

.. code-block:: ts

    import { useSelectedDelegatorStore } from 'stores/useSelectedDelegatorStore'
import useWalletOnePointOh from './useWalletOnePointOh'

export default function () {
  const wallet = useWalletOnePointOh()
  const selectedCommunityDelegator = useSelectedDelegatorStore(
    (s) => s.communityDelegator
  )

  // if we have a community token delegator selected (this is rare), use that. otherwise use user wallet.
  const owner =
    selectedCommunityDelegator !== undefined
      ? selectedCommunityDelegator
      : // I wanted to eliminate `null` as a possible type
        wallet?.publicKey ?? undefined
  return owner
}


