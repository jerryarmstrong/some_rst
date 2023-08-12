packages/governance-sdk/src/addins/serialisation.ts
===================================================

Last edited: 2023-07-19 16:40:40

Contents:

.. code-block:: ts

    import {
  GovernanceAddinAccountClass,
  MaxVoterWeightRecord,
  VoterWeightRecord,
} from './accounts';
import { BorshAccountParser } from '../core/serialisation';

export const GOVERNANCE_ADDINS_SCHEMA = new Map<any, any>([
  [
    MaxVoterWeightRecord,
    {
      kind: 'struct',
      fields: [
        ['accountDiscriminator', [8]],
        ['realm', 'pubkey'],
        ['governingTokenMint', 'pubkey'],
        ['maxVoterWeight', 'u64'],
        ['maxVoterWeightExpiry', { kind: 'option', type: 'u64' }],
      ],
    },
  ],
  [
    VoterWeightRecord,
    {
      kind: 'struct',
      fields: [
        ['accountDiscriminator', [8]],
        ['realm', 'pubkey'],
        ['governingTokenMint', 'pubkey'],
        ['governingTokenOwner', 'pubkey'],
        ['voterWeight', 'u64'],
        ['voterWeightExpiry', { kind: 'option', type: 'u64' }],
        ['weightAction', { kind: 'option', type: 'u8' }],
        ['weightActionTarget', { kind: 'option', type: 'pubkey' }],
      ],
    },
  ],
]);

export const GovernanceAddinAccountParser = (
  classType: GovernanceAddinAccountClass,
) => BorshAccountParser(classType, _ => GOVERNANCE_ADDINS_SCHEMA);


