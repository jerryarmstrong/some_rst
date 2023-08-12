hub/hooks/useProposal.ts
========================

Last edited: 2023-05-19 22:20:18

Contents:

.. code-block:: ts

    import { useContext } from 'react';

import { context } from '@hub/providers/Proposal';

/** @deprecated */
export function useProposal() {
  return useContext(context);
}


