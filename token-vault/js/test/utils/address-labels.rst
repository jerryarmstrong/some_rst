token-vault/js/test/utils/address-labels.ts
===========================================

Last edited: 2022-10-11 23:41:10

Contents:

.. code-block:: ts

    import { AddressLabels } from '@metaplex-foundation/amman';
import { VAULT_PROGRAM_ADDRESS } from '../../src/mpl-token-vault';
import { logDebug } from './log';

const persistLabelsPath = process.env.ADDRESS_LABEL_PATH;
const knownLabels = {
  [VAULT_PROGRAM_ADDRESS]: 'TokenVault',
};

export const addressLabels = new AddressLabels(knownLabels, logDebug, persistLabelsPath);


