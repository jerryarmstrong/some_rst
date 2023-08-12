next.config.js
==============

Last edited: 2022-08-19 10:41:17

Contents:

.. code-block:: js

    const withMarkdoc = require('@markdoc/next.js')
const { withPlausibleProxy } = require('next-plausible')

/** @type {import('next').NextConfig} */
const nextConfig = withMarkdoc()({
  swcMinify: true,
  reactStrictMode: true,
  pageExtensions: ['js', 'jsx', 'md'],
  experimental: {
    scrollRestoration: true,
    legacyBrowsers: false,
    images: { allowFutureImage: true },
  },
})

module.exports = withPlausibleProxy()(nextConfig)


