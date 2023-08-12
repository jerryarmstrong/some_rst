packages/governance/src/views/proposal/components/instructionInput/realmConfigForm.tsx
======================================================================================

Last edited: 2023-07-19 16:40:40

Contents:

.. code-block:: tsx

    import { Form, FormInstance, Input, InputNumber } from 'antd';
import { ExplorerLink, useMint, useWallet } from '@oyster/common';
import { Governance, GoverningTokenConfigAccountArgs, GoverningTokenType, PROGRAM_VERSION_V1, Realm } from '@solana/spl-governance';
import { PublicKey, TransactionInstruction } from '@solana/web3.js';
import React from 'react';

import { formDefaults } from '../../../../tools/forms';
import { useAnchorIdlAddress } from '../../../../tools/anchor/anchorHooks';

import { useRpcContext } from '../../../../hooks/useRpcContext';
import { createSetRealmConfig } from '@solana/spl-governance';
import Checkbox from 'antd/lib/checkbox/Checkbox';
import {
  parseMintSupplyFraction,
  RealmMintSupplyConfigFormItem,
  RealmMintSupplyConfigValues,
} from '../../../../components/realmMintSupplyConfigFormItem/realmMintSupplyConfigFormItem';
import BN from 'bn.js';
import {
  getMintDecimalAmountFromNatural,
  getMintMinAmountAsDecimal,
} from '../../../../tools/units';
import { parseMinTokensToCreate } from '../../../../components/governanceConfigFormItem/governanceConfigFormItem';
import { ProgramAccount } from '@solana/spl-governance';
import { voterWeightPluginValidator } from '../../../../tools/validators/voterWeightPlugin';

export interface RealmConfigValues {
  minCommunityTokensToCreateGovernance: number | string;
  communityMintDecimals: number;
}

class RealmConfigFormModel {
  minCommunityTokensToCreateGovernance: BN;

  constructor(args: { minCommunityTokensToCreateGovernance: BN }) {
    this.minCommunityTokensToCreateGovernance =
      args.minCommunityTokensToCreateGovernance;
  }
}

export function getRealmConfig(values: RealmConfigValues) {
  return new RealmConfigFormModel({
    minCommunityTokensToCreateGovernance: new BN(
      values.minCommunityTokensToCreateGovernance,
    ),
  });
}

export const RealmConfigForm = ({
  form,
  realm,
  governance,
  onCreateInstruction,
}: {
  form: FormInstance;
  realm: ProgramAccount<Realm>;
  governance: ProgramAccount<Governance>;
  onCreateInstruction: (instruction: TransactionInstruction) => void;
}) => {
  const idlAddress = useAnchorIdlAddress(governance.account.governedAccount);
  const { programId, programVersion } = useRpcContext();
  const wallet = useWallet();
  const communityMintInfo = useMint(realm?.account.communityMint);

  if (!wallet?.publicKey) {
    return <div>Wallet not connected</div>;
  }

  const onCreate = async (
    values: {
      removeCouncil: boolean;
      communityVoterWeightAddin: string | undefined;
    } & RealmMintSupplyConfigValues &
      RealmConfigValues,
  ) => {
    const minCommunityTokensToCreateGovernance = parseMinTokensToCreate(
      values.minCommunityTokensToCreateGovernance,
      values.communityMintDecimals,
    );

    const communityTokenConfig = values.communityVoterWeightAddin
    ? new GoverningTokenConfigAccountArgs({
      voterWeightAddin: new PublicKey(values.communityVoterWeightAddin),
      maxVoterWeightAddin: undefined,
      tokenType: GoverningTokenType.Liquid
    })
    : undefined;

    const setRealmConfigIx = await createSetRealmConfig(
      programId,
      programVersion,
      realm.pubkey,
      governance.pubkey,
      values.removeCouncil === true
        ? undefined
        : realm.account.config.councilMint,
      parseMintSupplyFraction(values.communityMintMaxVoteWeightFraction),
      // Use minCommunityTokensToCreateGovernance.toString() in case the number is larger than number
      new BN(minCommunityTokensToCreateGovernance.toString()),
      communityTokenConfig,
      undefined,
      // TODO: Once current wallet placeholder is supported to execute instruction using the wallet which executes the instruction replace it with the placeholder
      wallet.publicKey!,
    );

    onCreateInstruction(setRealmConfigIx);
  };

  const minCommunityTokenAmount = communityMintInfo
    ? getMintMinAmountAsDecimal(communityMintInfo)
    : 0;

  const minCommunityTokensToCreateGovernance = communityMintInfo
    ? getMintDecimalAmountFromNatural(
        communityMintInfo,
        realm.account.config.minCommunityTokensToCreateGovernance,
      ).toNumber()
    : 0;

  let mintDecimals = communityMintInfo ? communityMintInfo.decimals : 0;

  return (
    <Form
      {...formDefaults}
      form={form}
      onFinish={onCreate}
      initialValues={{ idlAccount: idlAddress }}
    >
      <Form.Item label="program id">
        <ExplorerLink address={programId} type="address" />
      </Form.Item>
      <Form.Item label="realm">
        <ExplorerLink address={realm.pubkey} type="address" />
      </Form.Item>
      <Form.Item label="realm authority (governance account)">
        <ExplorerLink address={governance.pubkey} type="address" />
      </Form.Item>

      {communityMintInfo && (
        <>
          <Form.Item
            label="min community tokens to create governance"
            name="minCommunityTokensToCreateGovernance"
            rules={[{ required: true }]}
            initialValue={minCommunityTokensToCreateGovernance}
          >
            <InputNumber
              min={minCommunityTokenAmount}
              // Do not restrict the max because teams might want to set it higher in anticipation of future mints
              // max={maxTokenAmount}
              step={minCommunityTokenAmount}
              style={{ width: 200 }}
              stringMode={mintDecimals !== 0}
            />
          </Form.Item>
          <Form.Item
            hidden
            name="communityMintDecimals"
            initialValue={communityMintInfo.decimals}
          ></Form.Item>
        </>
      )}

      {realm.account.config.councilMint && (
        <Form.Item
          label="remove council"
          name="removeCouncil"
          valuePropName="checked"
        >
          <Checkbox></Checkbox>
        </Form.Item>
      )}
      <RealmMintSupplyConfigFormItem
        communityMintAddress={realm.account.communityMint}
        maxVoteWeightSource={
          realm.account.config.communityMintMaxVoteWeightSource
        }
      ></RealmMintSupplyConfigFormItem>

      {programVersion > PROGRAM_VERSION_V1 && (
        <Form.Item
          name="communityVoterWeightAddin"
          label="community voter weight addin"
          rules={[{ required: false, validator: voterWeightPluginValidator }]}
        >
          <Input allowClear={true} />
        </Form.Item>
      )}
    </Form>
  );
};


