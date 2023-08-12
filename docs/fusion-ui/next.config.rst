next.config.js
==============

Last edited: 2023-02-28 18:04:35

Contents:

.. code-block:: js

    /** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
  swcMinify: true,
  images: {
    domains: ['shdw-drive.genesysgo.net'],
  }
}

module.exports = nextConfig


