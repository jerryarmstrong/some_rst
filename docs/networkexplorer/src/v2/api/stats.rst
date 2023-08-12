src/v2/api/stats.js
===================

Last edited: 2020-03-22 10:28:18

Contents:

.. code-block:: js

    import api from '.';

export function getStats() {
  return api('/global-stats');
}

export function getTxnStats() {
  return api('/txn-stats');
}

export function getClusterInfo() {
  return api('/cluster-info');
}


