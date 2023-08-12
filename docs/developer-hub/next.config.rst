next.config.js
==============

Last edited: 2023-08-11 10:00:06

Contents:

.. code-block:: js

    const withMarkdoc = require('@markdoc/next.js')

/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
  pageExtensions: ['js', 'jsx', 'md'],
  experimental: {
    scrollRestoration: true,
  },
}

module.exports = withMarkdoc({
  tokenizerOptions: { allowComments: true },
})(nextConfig)


