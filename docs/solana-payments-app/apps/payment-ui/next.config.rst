apps/payment-ui/next.config.js
==============================

Last edited: 2023-08-11 21:51:34

Contents:

.. code-block:: js

    // next.config.js
const nextConfig = {
    reactStrictMode: false,
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
    exportPathMap: function () {
        return {
            '/': { page: '/' },
            '/404': { page: '/404' },
            '/500': { page: '/500' },
        };
    },
};

module.exports = nextConfig;


