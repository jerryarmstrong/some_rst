apps/payment-ui/src/pages/_document.tsx
=======================================

Last edited: 2023-08-11 21:51:34

Contents:

.. code-block:: tsx

    import Document, { Head, Html, Main, NextScript } from 'next/document';

class MyDocument extends Document {
    render() {
        return (
            <Html lang="en">
                <Head>
                    <title>Solana Pay Payment Portal</title>
                    <meta name="description" content="Use Solana Pay for your Shopify Checkout" />
                    <link rel="icon" href="/favicon.ico" />
                </Head>
                <body>
                    <Main />
                    <NextScript />
                </body>
            </Html>
        );
    }
}

export default MyDocument;


