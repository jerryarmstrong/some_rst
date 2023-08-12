src/url.js
==========

Last edited: 2020-07-22 13:30:11

Contents:

.. code-block:: js

    import { testnetChannelEndpoint } from '@solana/web3.js';

const url = !process.env.LOCAL
  ? testnetChannelEndpoint(process.env.CHANNEL || 'stable', false)
  : 'http://localhost:8899';

export default url;


