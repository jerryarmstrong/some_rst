apps/backend-serverless/src/services/transaction-request/fetch-points-setup-transaction.service.ts
==================================================================================================

Last edited: 2023-08-11 21:51:34

Contents:

.. code-block:: ts

    import axios from 'axios';
import https from 'https';
import {
    TransactionRequestResponse,
    parseAndValidateTransactionRequestResponse,
} from '../../models/transaction-requests/transaction-request-response.model.js';
import { buildPointsSetupTransactionRequestEndpoint } from '../../utilities/transaction-request/endpoints.utility.js';

export const fetchPointsSetupTransaction = async (
    pointsMintAddress: string,
    gasAddress: string,
    feePayer: string,
    axiosInstance: typeof axios
): Promise<TransactionRequestResponse> => {
    const endpoint = buildPointsSetupTransactionRequestEndpoint(pointsMintAddress, feePayer, gasAddress);
    const headers = {
        'Content-Type': 'application/json',
    };

    let response;

    if (process.env.NODE_ENV === 'development') {
        const agent = new https.Agent({
            rejectUnauthorized: false,
        });

        response = await axios({
            url: endpoint,
            method: 'POST',
            headers: headers,
            httpsAgent: agent,
        });
    } else {
        response = await axios({
            url: endpoint,
            method: 'POST',
            headers: headers,
        });
    }

    if (response.status != 200) {
        throw new Error('Error fetching payment transaction.');
    }

    const paymentTransactionResponse = parseAndValidateTransactionRequestResponse(response.data);

    return paymentTransactionResponse;
};


