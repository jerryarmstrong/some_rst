apps/backend-serverless/src/models/websockets/connect.model.ts
==============================================================

Last edited: 2023-08-11 21:51:34

Contents:

.. code-block:: ts

    import { InferType, object, string } from 'yup';
import { parseAndValidateStrict } from '../../utilities/yup.utility.js';

export const connectSchema = object().shape({
    paymentId: string().required(),
});

export type ConnectParameters = InferType<typeof connectSchema>;

export const parseAndValidateConnectSchema = (connectSchemaBody: unknown): ConnectParameters => {
    return parseAndValidateStrict(
        connectSchemaBody,
        connectSchema,
        'Could not parse the merchant auth token body. Unknown Reason.',
    );
};


