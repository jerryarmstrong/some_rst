config/rollup-umd.js
====================

Last edited: 2020-08-13 15:30:25

Contents:

.. code-block:: js

    import config from './rollup'
import replace from 'rollup-plugin-replace'

config.plugins.push(
  replace({ 'process.env.NODE_ENV': JSON.stringify('development') })
)

config.output = {
  file: './umd/superstruct.js',
  format: 'umd',
  name: 'Superstruct',
}

export default config


