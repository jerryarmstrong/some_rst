js/packages/web/src/views/preLaunch/routes.tsx
==============================================

Last edited: 2022-06-29 06:18:54

Contents:

.. code-block:: tsx

    import React from 'react';
import { HashRouter, Route, Switch } from 'react-router-dom';
import { Providers } from './providers';

import { PreLaunchView } from './';

export function Routes() {
  return (
    <>
      <HashRouter basename={'/'}>
        <Providers>
          <Switch>
            <Route path="/" component={() => <PreLaunchView />} />
          </Switch>
        </Providers>
      </HashRouter>
    </>
  );
}


