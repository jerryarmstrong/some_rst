pages/dao/[symbol]/members/index.tsx
====================================

Last edited: 2023-08-11 18:13:34

Contents:

.. code-block:: tsx

    import Members from './Members'
import { useRealmConfigQuery } from '@hooks/queries/realmConfig'
const MembersPage = () => {
  const config = useRealmConfigQuery().data?.result
  return (
    <div>
      {!config?.account.communityTokenConfig.voterWeightAddin ? (
        <Members />
      ) : null}
    </div>
  )
}

export default MembersPage


