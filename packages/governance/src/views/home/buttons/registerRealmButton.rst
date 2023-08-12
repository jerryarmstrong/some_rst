packages/governance/src/views/home/buttons/registerRealmButton.tsx
==================================================================

Last edited: 2023-07-19 16:40:40

Contents:

.. code-block:: tsx

    import React, { useState } from 'react';
import { ButtonProps, Collapse, Switch, Typography } from 'antd';
import { Form, Input } from 'antd';
import { PublicKey } from '@solana/web3.js';

import { LABELS } from '../../../constants';

import { Redirect } from 'react-router';
import { MintFormItem } from '../../../components/MintFormItem/mintFormItem';

import { registerRealm } from '../../../actions/registerRealm';

import { ModalFormAction } from '../../../components/ModalFormAction/modalFormAction';
import { useRpcContext } from '../../../hooks/useRpcContext';
import { getRealmUrl } from '../../../tools/routeTools';
import {
  MintMaxVoteWeightSource,
  MintMaxVoteWeightSourceType,
  PROGRAM_VERSION_V1,
} from '@solana/spl-governance';

import { BigNumber } from 'bignumber.js';

import { BN } from 'bn.js';
import {
  RealmMintSupplyConfigFormItem,
  RealmMintSupplyConfigValues,
} from '../../../components/realmMintSupplyConfigFormItem/realmMintSupplyConfigFormItem';
import { RealmMintTokensFormItem } from '../../../components/realmMintTokensFormItem/realmMintTokensFormItem';
import { parseMinTokensToCreate } from '../../../components/governanceConfigFormItem/governanceConfigFormItem';

import { voterWeightPluginValidator } from '../../../tools/validators/voterWeightPlugin';

const { Panel } = Collapse;
const { Text } = Typography;

const parseMintSupplyFraction = (fraction: string) => {
  if (!fraction) {
    return MintMaxVoteWeightSource.FULL_SUPPLY_FRACTION;
  }

  const fractionValue = new BigNumber(fraction)
    .shiftedBy(MintMaxVoteWeightSource.SUPPLY_FRACTION_DECIMALS)
    .toNumber();

  return new MintMaxVoteWeightSource({
    type: MintMaxVoteWeightSourceType.SupplyFraction,
    value: new BN(fractionValue),
  });
};

export function RegisterRealmButton({
  buttonProps,
}: {
  buttonProps: ButtonProps;
}) {
  const [redirectTo, setRedirectTo] = useState('');
  const rpcContext = useRpcContext();
  const { programId, programVersion } = rpcContext;

  const [councilVisible, setCouncilVisible] = useState(false);

  const [communityMintAddress, setCommunityMintAddress] = useState('');
  const [communityVoterWeightAddin, setCommunityVoterWeightAddin] =
    useState('');

  const onSubmit = async (
    values: {
      communityMint: string;
      councilMint: string;
      name: string;
      useCouncilMint: boolean;
      mintDecimals: number;
      minTokensToCreateGovernance: number | string;
      communityVoterWeightAddin: string;
    } & RealmMintSupplyConfigValues,
  ) => {
    let supplyFraction = parseMintSupplyFraction(
      values.communityMintMaxVoteWeightFraction,
    );

    const minCommunityTokensToCreateGovernance = parseMinTokensToCreate(
      values.minTokensToCreateGovernance,
      values.mintDecimals,
    );

    return await registerRealm(
      rpcContext,
      values.name,
      new PublicKey(values.communityMint),
      values.useCouncilMint ? new PublicKey(values.councilMint) : undefined,
      supplyFraction,
      new BN(minCommunityTokensToCreateGovernance),
      communityVoterWeightAddin
        ? new PublicKey(communityVoterWeightAddin)
        : undefined,
    );
  };

  const onComplete = (pk: PublicKey) => {
    setRedirectTo(pk.toBase58());
  };

  const onReset = () => {
    setCouncilVisible(false);
  };

  if (redirectTo) {
    return <Redirect push to={getRealmUrl(redirectTo, programId)} />;
  }

  return (
    <ModalFormAction<PublicKey>
      label="Register Realm"
      buttonProps={buttonProps}
      formTitle="Register Realm"
      formAction="Register"
      formPendingAction="Registering"
      onSubmit={onSubmit}
      onComplete={onComplete}
      onReset={onReset}
      initialValues={{
        useCouncilMint: false,
      }}
    >
      <Form.Item
        name="name"
        label={LABELS.NAME_LABEL}
        rules={[{ required: true }]}
      >
        <Input />
      </Form.Item>

      <MintFormItem
        name="communityMint"
        label={LABELS.COMMUNITY_TOKEN_MINT}
        onChange={mint => setCommunityMintAddress(mint)}
      ></MintFormItem>

      <RealmMintTokensFormItem
        communityMintAddress={communityMintAddress}
      ></RealmMintTokensFormItem>

      <Form.Item
        name="useCouncilMint"
        label={LABELS.USE_COUNCIL_TOKEN}
        valuePropName="checked"
      >
        <Switch onChange={setCouncilVisible} />
      </Form.Item>
      {councilVisible && (
        <MintFormItem
          name="councilMint"
          label={LABELS.COUNCIL_TOKEN_MINT}
          required={councilVisible}
        />
      )}

      <Collapse ghost>
        <Panel
          header={<Text type="secondary">advance settings</Text>}
          key="1"
          className="realm-advance-settings-panel"
        >
          <RealmMintSupplyConfigFormItem
            communityMintAddress={communityMintAddress}
            maxVoteWeightSource={MintMaxVoteWeightSource.FULL_SUPPLY_FRACTION}
          ></RealmMintSupplyConfigFormItem>

          {programVersion > PROGRAM_VERSION_V1 && (
            <Form.Item
              name="communityVoterWeightAddin"
              label="community voter weight addin"
              rules={[
                { required: false, validator: voterWeightPluginValidator },
              ]}
            >
              <Input
                allowClear={true}
                onChange={e => setCommunityVoterWeightAddin(e.target.value)}
              />
            </Form.Item>
          )}
        </Panel>
      </Collapse>
    </ModalFormAction>
  );
}


