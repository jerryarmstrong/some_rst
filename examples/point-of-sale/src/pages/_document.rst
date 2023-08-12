examples/point-of-sale/src/pages/_document.tsx
==============================================

Last edited: 2023-05-03 15:27:33

Contents:

.. code-block:: tsx

    import { Head, Html, Main, NextScript } from 'next/document';

export default function Document() {
    return (
        <Html style={{ visibility: 'hidden' }}>
            <Head />
            <body>
                <Main />
                <NextScript />
            </body>
        </Html>
    );
}


