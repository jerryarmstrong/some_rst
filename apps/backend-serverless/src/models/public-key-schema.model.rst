apps/backend-serverless/src/models/public-key-schema.model.ts
=============================================================

Last edited: 2023-08-11 21:51:34

Contents:

.. code-block:: ts

    import * as web3 from '@solana/web3.js';
import { string } from 'yup';

export const publicKeySchema = string().test('is-public-key', 'Invalid public key', value => {
    try {
        if (value === undefined || value === null) {
            return true;
        }
        new web3.PublicKey(value);
        return true;
    } catch (err) {
        return false;
    }
});


