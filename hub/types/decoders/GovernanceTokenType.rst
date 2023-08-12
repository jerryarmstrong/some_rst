hub/types/decoders/GovernanceTokenType.ts
=========================================

Last edited: 2023-08-11 18:13:34

Contents:

.. code-block:: ts

    import * as IT from 'io-ts';

import { GovernanceTokenType as _GovernanceTokenType } from '../GovernanceTokenType';

export const GovernanceTokenTypeCouncil = IT.literal(
  _GovernanceTokenType.Council,
);
export const GovernanceTokenTypeCommunity = IT.literal(
  _GovernanceTokenType.Community,
);

export const GovernanceTokenType = IT.union([
  GovernanceTokenTypeCouncil,
  GovernanceTokenTypeCommunity,
]);


