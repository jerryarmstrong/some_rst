js/packages/web/src/pages/index.tsx
===================================

Last edited: 2022-06-29 06:18:54

Contents:

.. code-block:: tsx

    import dynamic from 'next/dynamic';
import React from 'react';

const CreateReactAppEntryPoint = dynamic(() => import('../App'), {
  ssr: false,
});

function App() {
  return <CreateReactAppEntryPoint />;
}

export default App;


