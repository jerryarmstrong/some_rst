examples/point-of-sale/next.config.js
=====================================

Last edited: 2023-05-03 15:27:33

Contents:

.. code-block:: js

    /** @type {import('next').NextConfig} */
const nextConfig = {
    reactStrictMode: true,
    async redirects() {
        return [
            {
                source: '/',
                destination: '/new',
                permanent: false,
                has: [
                    {
                        type: 'query',
                        key: 'recipient',
                    },
                    {
                        type: 'query',
                        key: 'label',
                    },
                ],
            },
        ];
    },
};

module.exports = nextConfig;


