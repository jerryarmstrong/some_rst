pages/dao/[symbol]/vsrWithdraw/[tokenOwnerRecordPk].tsx
=======================================================

Last edited: 2023-08-11 18:13:34

Contents:

.. code-block:: tsx

    import { useRouter } from 'next/router'
import LockTokensAccountWithdraw from 'VoteStakeRegistry/components/Account/LockTokensAccountWithdraw'

const AccountViewPage = () => {
  const router = useRouter()

  const tokenOwnerRecordPk = router.query?.tokenOwnerRecordPk

  return (
    typeof tokenOwnerRecordPk === 'string' && (
      <LockTokensAccountWithdraw
        tokenOwnerRecordPk={tokenOwnerRecordPk}
      ></LockTokensAccountWithdraw>
    )
  )
}

export default AccountViewPage


