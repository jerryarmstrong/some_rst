apps/backend-serverless/src/models/transaction-requests/transaction-request-response.model.ts
=============================================================================================

Last edited: 2023-08-11 21:51:34

Contents:

.. code-block:: ts

    import { InferType, object, string } from 'yup';
import { parseAndValidateStrict } from '../../utilities/yup.utility.js';

export const transactionRequestResponseScheme = object().shape({
    transaction: string().required(),
    message: string().optional(),
});

export type TransactionRequestResponse = InferType<typeof transactionRequestResponseScheme>;

export const parseAndValidateTransactionRequestResponse = (
    transactionRequestResponseBody: unknown,
): TransactionRequestResponse => {
    return parseAndValidateStrict<TransactionRequestResponse>(
        transactionRequestResponseBody,
        transactionRequestResponseScheme,
        'Could not parse the transaction request response. Unknown Reason.',
    );
};


