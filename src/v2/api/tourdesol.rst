src/v2/api/tourdesol.js
=======================

Last edited: 2020-03-22 10:28:18

Contents:

.. code-block:: js

    import _ from 'lodash';

import api from '.';

const TOURDESOL_INDEX_VERSION = 'TourDeSolIndexView@1.0.0';

export function apiGetTourDeSolIndexPage({version, activeStage, demo}) {
  const queryString = _.toPairs({
    v: version || TOURDESOL_INDEX_VERSION,
    activeStage: activeStage || 0,
    isDemo: demo || false,
  })
    .map(([k, v]) => `${k}=${encodeURIComponent(v)}`)
    .join('&');

  return api(`/explorer/tourdesol/index?${queryString}`);
}


