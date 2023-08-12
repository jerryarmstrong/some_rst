apps/backend-serverless/src/utilities/responses/request-response.utility.ts
===========================================================================

Last edited: 2023-08-11 21:51:34

Contents:

.. code-block:: ts

    export const requestErrorResponse = (error: unknown) => {
    if (error instanceof Error) {
        return {
            statusCode: 500,
            body: JSON.stringify(
                {
                    error: error.message,
                },
                null,
                2,
            ),
        };
    } else {
        return {
            statusCode: 500,
            body: JSON.stringify(
                {
                    error: 'Unknown Error',
                },
                null,
                2,
            ),
        };
    }
};


