config/rollup-cjs.js
====================

Last edited: 2020-08-13 15:30:25

Contents:

.. code-block:: js

    import config from './rollup'

config.output = {
  file: './lib/index.cjs',
  format: 'cjs',
  name: 'Superstruct',
  sourcemap: true,
}

export default config


