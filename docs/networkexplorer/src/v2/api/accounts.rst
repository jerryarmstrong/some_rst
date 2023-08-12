src/v2/api/accounts.js
======================

Last edited: 2020-03-22 10:28:18

Contents:

.. code-block:: js

    import _ from 'lodash';

import api from '.';

const DEFAULT_PAGE_SIZE = 100;

const ACCOUNT_DETAIL_VERSION = 'AccountDetailView@1.0.0';

export function apiGetAccountDetail({accountId, version}) {
  return api(
    `/explorer/accounts/${encodeURIComponent(accountId)}?v=${version ||
      ACCOUNT_DETAIL_VERSION}`,
  );
}

const ACCOUNT_INDEX_VERSION = 'AccountIndexView@1.0.0';

export function apiGetAccountsTimelinePage({
  start = '',
  count = DEFAULT_PAGE_SIZE,
  direction = '-',
  version,
}) {
  const queryString = _.toPairs({
    start,
    count,
    direction,
    v: version || ACCOUNT_INDEX_VERSION,
  })
    .map(([k, v]) => `${k}=${encodeURIComponent(v)}`)
    .join('&');

  return api(`/explorer/accounts/index?${queryString}`);
}


