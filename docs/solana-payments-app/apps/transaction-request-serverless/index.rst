apps/transaction-request-serverless/index.js
============================================

Last edited: 2023-08-11 21:51:34

Contents:

.. code-block:: js

    module.exports.handler = async event => {
    return {
        statusCode: 200,
        body: JSON.stringify(
            {
                message: 'Go Serverless v3.0! Your function executed successfully!',
                input: event,
            },
            null,
            2,
        ),
    };
};


