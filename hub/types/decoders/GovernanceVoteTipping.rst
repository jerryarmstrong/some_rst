hub/types/decoders/GovernanceVoteTipping.ts
===========================================

Last edited: 2023-08-11 18:13:34

Contents:

.. code-block:: ts

    import * as IT from 'io-ts';

import { GovernanceVoteTipping as _GovernanceVoteTipping } from '../GovernanceVoteTipping';

export const GovernanceVoteTippingDisabled = IT.literal(
  _GovernanceVoteTipping.Disabled,
);
export const GovernanceVoteTippingEarly = IT.literal(
  _GovernanceVoteTipping.Early,
);
export const GovernanceVoteTippingStrict = IT.literal(
  _GovernanceVoteTipping.Strict,
);

export const GovernanceVoteTipping = IT.union([
  GovernanceVoteTippingDisabled,
  GovernanceVoteTippingEarly,
  GovernanceVoteTippingStrict,
]);


