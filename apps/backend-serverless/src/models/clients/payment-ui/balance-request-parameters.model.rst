apps/backend-serverless/src/models/clients/payment-ui/balance-request-parameters.model.ts
=========================================================================================

Last edited: 2023-08-11 21:51:34

Contents:

.. code-block:: ts

    import { InferType, object } from 'yup';
import { parseAndValidateStrict } from '../../../utilities/yup.utility.js';
import { publicKeySchema } from '../../public-key-schema.model.js';

export const balanceRequestParametersScheme = object().shape({
    publicKey: publicKeySchema.required(),
    mint: publicKeySchema.required(),
});

export type BalanceRequestParameters = InferType<typeof balanceRequestParametersScheme>;

export const parseAndValidateBalanceParameters = (balanceRequestParameters: unknown): BalanceRequestParameters => {
    return parseAndValidateStrict(
        balanceRequestParameters,
        balanceRequestParametersScheme,
        'Can not parse balance parameters. Unkownn reason.'
    );
};


