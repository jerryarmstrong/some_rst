apps/merchant-ui/next.config.js
===============================

Last edited: 2023-08-11 21:51:34

Contents:

.. code-block:: js

    /** @type {import('next').NextConfig} */
const nextConfig = {
    reactStrictMode: true,
    images: {
        remotePatterns: [
            {
                protocol: 'https',
                hostname: 'cdn.shopify.com',
                port: '',
                pathname: '/s/files/**',
            },
            {
                protocol: 'https',
                hostname: 'arweave.net',
                port: '',
                pathname: '/**',
            },
        ],
    },
};

module.exports = nextConfig;


