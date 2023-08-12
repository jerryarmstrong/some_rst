url.js
======

Last edited: 2020-07-29 22:45:43

Contents:

.. code-block:: js

    // @noflow

import {testnetChannelEndpoint} from '@solana/web3.js';

export let url = process.env.LIVE
  ? testnetChannelEndpoint(process.env.CHANNEL || 'stable', false)
  : 'http://localhost:8899';

export let urlTls = process.env.LIVE
  ? testnetChannelEndpoint(process.env.CHANNEL || 'stable', true)
  : 'http://localhost:8899';


