packages/governance/src/views/proposal/components/instructionInput/governanceInstructionForm.tsx
================================================================================================

Last edited: 2023-07-19 16:40:40

Contents:

.. code-block:: tsx

    import { FormInstance } from 'antd';
import React from 'react';

import { Governance, PROGRAM_VERSION_V1, Realm } from '@solana/spl-governance';
import { GovernanceConfigForm } from './governanceConfigForm';
import { InstructionType } from './instructionSelector';
import { TransactionInstruction } from '@solana/web3.js';
import { RealmConfigForm } from './realmConfigForm';
import { NativeTransferForm } from './nativeTokenTransferForm';
import { ProgramAccount } from '@solana/spl-governance';
import { VoterStakeCreateRegistrarForm } from './voterStakeRegistry/voterStakeCreateRegistrarForm';
import { VoterStakeConfigureMintForm } from './voterStakeRegistry/voterStakeConfigureMintForm';
import { SetRealmAuthorityForm } from './setRealmAuthority';

export function getGovernanceInstructions(
  programVersion: number,
  realm: ProgramAccount<Realm>,
  governance: ProgramAccount<Governance>,
) {
  let instructions = [InstructionType.GovernanceSetConfig];

  if (governance.pubkey.toBase58() === realm.account.authority?.toBase58()) {
    instructions.push(InstructionType.SetRealmConfig);
    instructions.push(InstructionType.SetRealmAuthority);

    if (programVersion > PROGRAM_VERSION_V1) {
      instructions.push(InstructionType.VoterStakeCreateRegistrar);
      instructions.push(InstructionType.VoterStakeConfigureMint);
    }
  }

  return instructions;
}

export function GovernanceInstructionForm({
  form,
  instruction,
  realm,
  governance,
  onCreateInstruction,
}: {
  form: FormInstance;
  instruction: InstructionType;
  realm: ProgramAccount<Realm>;
  governance: ProgramAccount<Governance>;
  onCreateInstruction: (instruction: TransactionInstruction) => void;
}) {
  return (
    <>
      {instruction === InstructionType.NativeTransfer && (
        <NativeTransferForm
          form={form}
          governance={governance}
          onCreateInstruction={onCreateInstruction}
        ></NativeTransferForm>
      )}

      {instruction === InstructionType.GovernanceSetConfig && (
        <GovernanceConfigForm
          form={form}
          governance={governance}
          onCreateInstruction={onCreateInstruction}
        ></GovernanceConfigForm>
      )}
      {instruction === InstructionType.SetRealmConfig && (
        <RealmConfigForm
          form={form}
          realm={realm}
          governance={governance}
          onCreateInstruction={onCreateInstruction}
        ></RealmConfigForm>
      )}
      {instruction === InstructionType.SetRealmAuthority && (
        <SetRealmAuthorityForm
          form={form}
          realm={realm}
          governance={governance}
          onCreateInstruction={onCreateInstruction}
        ></SetRealmAuthorityForm>
      )}
      {instruction === InstructionType.VoterStakeCreateRegistrar && (
        <VoterStakeCreateRegistrarForm
          form={form}
          realm={realm}
          governance={governance}
          onCreateInstruction={onCreateInstruction}
        ></VoterStakeCreateRegistrarForm>
      )}
      {instruction === InstructionType.VoterStakeConfigureMint && (
        <VoterStakeConfigureMintForm
          form={form}
          realm={realm}
          governance={governance}
          onCreateInstruction={onCreateInstruction}
        ></VoterStakeConfigureMintForm>
      )}
    </>
  );
}


