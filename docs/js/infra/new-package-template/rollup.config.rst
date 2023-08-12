infra/new-package-template/rollup.config.js
===========================================

Last edited: 2023-05-26 09:49:40

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


