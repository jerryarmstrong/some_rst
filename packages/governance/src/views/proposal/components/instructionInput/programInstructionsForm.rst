packages/governance/src/views/proposal/components/instructionInput/programInstructionsForm.tsx
==============================================================================================

Last edited: 2023-07-19 16:40:40

Contents:

.. code-block:: tsx

    import { Form, FormInstance } from 'antd';

import { Governance, Realm } from '@solana/spl-governance';
import { TransactionInstruction } from '@solana/web3.js';
import React, { useState } from 'react';

import { formDefaults } from '../../../../tools/forms';
import { ProgramUpgradeForm } from './programUpgradeForm';
import { AnchorIdlSetBufferForm } from './anchorIdlSetBufferForm';
import { useAnchorIdlAccount } from '../../../../tools/anchor/anchorHooks';

import { InstructionSelector, InstructionType } from './instructionSelector';
import {
  getGovernanceInstructions,
  GovernanceInstructionForm,
} from './governanceInstructionForm';
import { ProgramAccount } from '@solana/spl-governance';

export const ProgramInstructionsForm = ({
  programVersion,
  form,
  realm,
  governance,
  onCreateInstruction,
  coreInstructions,
}: {
  programVersion: number;
  form: FormInstance;
  realm: ProgramAccount<Realm>;
  governance: ProgramAccount<Governance>;
  onCreateInstruction: (instruction: TransactionInstruction) => void;
  coreInstructions: InstructionType[];
}) => {
  const [instruction, setInstruction] = useState(
    InstructionType.UpgradeProgram,
  );

  const anchorIdlAccount = useAnchorIdlAccount(
    governance.account.governedAccount,
  );

  let anchorInstructions = anchorIdlAccount
    ? [InstructionType.AnchorIDLSetBuffer]
    : [];

  // TODO: filter available instructions based on the already included into a Proposal
  let instructions = [
    InstructionType.UpgradeProgram,
    ...coreInstructions,
    ...anchorInstructions,
    ...getGovernanceInstructions(programVersion, realm, governance),
  ];

  return (
    <Form
      {...formDefaults}
      initialValues={{ instructionType: instructions[0] }}
    >
      <InstructionSelector
        instructions={instructions}
        onChange={setInstruction}
      ></InstructionSelector>
      {instruction === InstructionType.UpgradeProgram && (
        <ProgramUpgradeForm
          form={form}
          governance={governance}
          onCreateInstruction={onCreateInstruction}
        ></ProgramUpgradeForm>
      )}
      {instruction === InstructionType.AnchorIDLSetBuffer && (
        <AnchorIdlSetBufferForm
          form={form}
          governance={governance}
          onCreateInstruction={onCreateInstruction}
        ></AnchorIdlSetBufferForm>
      )}

      <GovernanceInstructionForm
        form={form}
        realm={realm}
        governance={governance}
        onCreateInstruction={onCreateInstruction}
        instruction={instruction}
      ></GovernanceInstructionForm>
    </Form>
  );
};


