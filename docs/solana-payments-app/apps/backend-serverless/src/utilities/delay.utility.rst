apps/backend-serverless/src/utilities/delay.utility.ts
======================================================

Last edited: 2023-08-11 21:51:34

Contents:

.. code-block:: ts

    export function delay(ms: number) {
    return new Promise(resolve => setTimeout(resolve, ms));
}


