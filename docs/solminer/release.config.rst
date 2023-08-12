release.config.js
=================

Last edited: 2020-07-22 13:30:11

Contents:

.. code-block:: js

    module.exports = {
  plugins: [
    '@semantic-release/commit-analyzer',
    '@semantic-release/release-notes-generator',
    [
      '@semantic-release/github',
      {
        assets: [],
      },
    ],
  ],
};


