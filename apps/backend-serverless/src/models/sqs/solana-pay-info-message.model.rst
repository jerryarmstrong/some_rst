apps/backend-serverless/src/models/sqs/solana-pay-info-message.model.ts
=======================================================================

Last edited: 2023-08-11 21:51:34

Contents:

.. code-block:: ts

    import { InferType, object, string } from 'yup';
import { parseAndValidateStrict } from '../../utilities/yup.utility.js';

export const solanaPayInfoMessageSchema = object().shape({
    account: string().required(),
    paymentRecordId: string().required(),
});

export type SolanaPayInfoMessage = InferType<typeof solanaPayInfoMessageSchema>;

export const parseAndValidateSolanaPayInfoMessage = (solanaPayInfoMessageBody: unknown): SolanaPayInfoMessage => {
    return parseAndValidateStrict(
        solanaPayInfoMessageBody,
        solanaPayInfoMessageSchema,
        'Could not parse the solana pay info message body. Unknown Reason.',
    );
};


