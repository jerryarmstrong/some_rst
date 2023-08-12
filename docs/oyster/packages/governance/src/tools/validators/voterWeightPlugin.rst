packages/governance/src/tools/validators/voterWeightPlugin.ts
=============================================================

Last edited: 2023-07-19 16:40:40

Contents:

.. code-block:: ts

    import { tryParseKey } from '@oyster/common';

export const voterWeightPluginValidator = async (rule: any, value: string) => {
  if (value) {
    const pubkey = tryParseKey(value);

    if (!pubkey) {
      throw new Error('Provided value is not a valid publickey');
    }
  }
};


