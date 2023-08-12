packages/starter/material-ui-starter/src/index.tsx
==================================================

Last edited: 2023-08-07 04:48:35

Contents:

.. code-block:: tsx

    import React, { StrictMode } from 'react';
import { createRoot } from 'react-dom/client';
import { App } from './App';

// eslint-disable-next-line @typescript-eslint/no-non-null-assertion
createRoot(document.getElementById('app')!).render(
    <StrictMode>
        <App />
    </StrictMode>
);


