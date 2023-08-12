apps/backend-serverless/src/models/transaction-requests/transaction-request-body.model.ts
=========================================================================================

Last edited: 2023-08-11 21:51:34

Contents:

.. code-block:: ts

    import { InferType, object } from 'yup';
import { parseAndValidateStrict } from '../../utilities/yup.utility.js';
import { publicKeySchema } from '../public-key-schema.model.js';

export const transactionRequestBodySchema = object().shape({
    account: publicKeySchema.required(),
});

export type TransactionRequestBody = InferType<typeof transactionRequestBodySchema>;

export const parseAndValidateTransactionRequestBody = (transactionRequestBody: unknown): TransactionRequestBody => {
    return parseAndValidateStrict<TransactionRequestBody>(
        transactionRequestBody,
        transactionRequestBodySchema,
        'Could not parse the transaction request body. Unknown Reason.'
    );
};


