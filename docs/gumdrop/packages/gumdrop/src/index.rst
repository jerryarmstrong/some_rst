packages/gumdrop/src/index.tsx
==============================

Last edited: 2022-08-25 19:21:42

Contents:

.. code-block:: tsx

    import * as React from 'react';
import { render } from 'react-dom';
import App from './components/App';

import './styles/index.less';

const rootEl = document.getElementById('root');

render(<App />, rootEl);


