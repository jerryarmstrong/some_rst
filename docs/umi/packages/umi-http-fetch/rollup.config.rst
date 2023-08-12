packages/umi-http-fetch/rollup.config.js
========================================

Last edited: 2023-07-27 15:49:41

Contents:

.. code-block:: js

    import { createConfigs } from '../../rollup.config';
import pkg from './package.json';

export default createConfigs({
  pkg,
  builds: [
    {
      dir: 'dist/esm',
      format: 'es',
    },
    {
      dir: 'dist/cjs',
      format: 'cjs',
    },
  ],
});


