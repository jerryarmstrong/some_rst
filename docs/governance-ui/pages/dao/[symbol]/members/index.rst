pages/dao/[symbol]/members/index.tsx
====================================

Last edited: 2023-05-19 22:20:18

Contents:

.. code-block:: tsx

    import useRealm from '@hooks/useRealm'
import Members from './Members'
const MembersPage = () => {
  const { config } = useRealm()
  return (
    <div>
      {!config?.account.communityTokenConfig.voterWeightAddin ? (
        <Members />
      ) : null}
    </div>
  )
}

export default MembersPage


