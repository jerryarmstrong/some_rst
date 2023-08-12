packages/governance/src/views/proposal/components/instructionInput/accountInstructionsForm.tsx
==============================================================================================

Last edited: 2023-07-19 16:40:40

Contents:

.. code-block:: tsx

    import { Form, FormInstance } from 'antd';

import { Governance, Realm } from '@solana/spl-governance';
import { TransactionInstruction } from '@solana/web3.js';
import React, { useState } from 'react';

import { formDefaults } from '../../../../tools/forms';

import { InstructionSelector, InstructionType } from './instructionSelector';
import {
  getGovernanceInstructions,
  GovernanceInstructionForm,
} from './governanceInstructionForm';
import { ProgramAccount } from '@solana/spl-governance';

export const AccountInstructionsForm = ({
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
  const [instruction, setInstruction] = useState<InstructionType | undefined>();

  let instructions = [
    ...coreInstructions,
    ...getGovernanceInstructions(programVersion, realm, governance),
  ];

  if (!instruction) {
    setInstruction(instructions[0]);
    return null;
  }

  return (
    <Form
      {...formDefaults}
      initialValues={{ instructionType: instructions[0] }}
    >
      <InstructionSelector
        instructions={instructions}
        onChange={setInstruction}
      ></InstructionSelector>

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


