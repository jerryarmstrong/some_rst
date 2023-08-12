packages/governance/src/views/home/buttons/updateProgramMetadataButton.tsx
==========================================================================

Last edited: 2023-07-19 16:40:40

Contents:

.. code-block:: tsx

    import React from 'react';

import { useRpcContext } from '../../../hooks/useRpcContext';

import { ModalFormAction } from '../../../components/ModalFormAction/modalFormAction';

import { updateProgramMetadata } from '../../../actions/updateProgramMetadata';
import { PROGRAM_VERSION_V1 } from '@solana/spl-governance';

export function UpdateProgramMetadataButton() {
  const rpcContext = useRpcContext();

  const onSubmit = async () => {
    await updateProgramMetadata(rpcContext!);
  };

  return (
    <ModalFormAction<void>
      label="Update Program Metadata"
      formTitle="Update Program Metadata"
      formAction="Update"
      formPendingAction="Updating"
      onSubmit={() => onSubmit()}
      buttonProps={{
        disabled: rpcContext.programVersion <= PROGRAM_VERSION_V1,
      }}
    >
      <div>Update Program Metadata</div>
    </ModalFormAction>
  );
}


