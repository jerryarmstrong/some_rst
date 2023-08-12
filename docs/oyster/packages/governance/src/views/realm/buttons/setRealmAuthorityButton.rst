packages/governance/src/views/realm/buttons/setRealmAuthorityButton.tsx
=======================================================================

Last edited: 2023-07-19 16:40:40

Contents:

.. code-block:: tsx

    import React from 'react';
import { Realm } from '@solana/spl-governance';

import { PublicKey } from '@solana/web3.js';
import { useRpcContext } from '../../../hooks/useRpcContext';
import { ModalFormAction } from '../../../components/ModalFormAction/modalFormAction';

import { setRealmAuthority } from '../../../actions/setRealmAuthority';
import { Form, Select } from 'antd';
import { useGovernancesByRealm } from '../../../hooks/apiHooks';
import { ProgramAccount } from '@solana/spl-governance';

export function SetRealmAuthorityButton({
  realm,
}: {
  realm: ProgramAccount<Realm>;
}) {
  const rpcContext = useRpcContext();
  const governances = useGovernancesByRealm(realm?.pubkey);

  const onSubmit = async (values: { realmAuthority: string }) => {
    const realmAuthority = new PublicKey(values.realmAuthority);

    await setRealmAuthority(rpcContext, realm, realmAuthority);

    return realmAuthority;
  };

  return (
    <ModalFormAction<PublicKey>
      label="Set Realm Authority"
      formTitle="Set Realm Authority"
      formAction="Set Authority"
      formPendingAction="Setting Authority"
      onSubmit={onSubmit}
      initialValues={{ useCouncilMint: false }}
    >
      <Form.Item
        name="realmAuthority"
        label="realm authority governance"
        rules={[{ required: true }]}
      >
        <Select>
          {governances.map(g => (
            <Select.Option
              value={g.pubkey.toBase58()}
              key={g.pubkey.toBase58()}
            >
              {g.account.governedAccount.toBase58()}
            </Select.Option>
          ))}
        </Select>
      </Form.Item>
    </ModalFormAction>
  );
}


