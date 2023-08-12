src/index.js
============

Last edited: 2020-03-22 10:28:18

Contents:

.. code-block:: js

    import React, {lazy, Suspense} from 'react';
import ReactDOM from 'react-dom';
import {BrowserRouter} from 'react-router-dom';

import './index.css';
import App from './App';
import * as serviceWorker from './serviceWorker';
import * as EndpointConfig from './EndpointConfig';
import ScrollToTop from './v2/components/ScrollToTop';
const AppV2 = lazy(() => import('./AppV2'));

async function main() {
  await EndpointConfig.load();
  const renderV1 = window.location.pathname.startsWith('/v1');
  ReactDOM.render(
    <BrowserRouter basename={renderV1 ? '/v1' : null}>
      {renderV1 ? (
        <App />
      ) : (
        <Suspense fallback={<div>Loading...</div>}>
          <ScrollToTop>
            <AppV2 />
          </ScrollToTop>
        </Suspense>
      )}
    </BrowserRouter>,
    document.getElementById('root'),
  );
}
main();

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: http://bit.ly/CRA-PWA
serviceWorker.unregister();


