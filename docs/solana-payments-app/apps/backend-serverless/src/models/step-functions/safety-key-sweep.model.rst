apps/backend-serverless/src/models/step-functions/safety-key-sweep.model.ts
===========================================================================

Last edited: 2023-08-11 21:51:34

Contents:

.. code-block:: ts

    import { InferType, object, string } from 'yup';
import { parseAndValidateStrict } from '../../utilities/yup.utility.js';

export const safetyKeyMessageSchema = object().shape({
    key: string().required(),
});

export type SafetyKeyMessage = InferType<typeof safetyKeyMessageSchema>;

export const parseAndValidateSafetyKeyMessage = (safetyKeyMessageBody: unknown): SafetyKeyMessage => {
    return parseAndValidateStrict(
        safetyKeyMessageBody,
        safetyKeyMessageSchema,
        'Could not parse the safety key message. Unknown Reason.',
    );
};


