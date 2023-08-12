packages/build-scripts/tsup.config.browser.ts
=============================================

Last edited: 2023-08-11 09:49:26

Contents:

.. code-block:: ts

    import { defineConfig } from 'tsup';

import { getBaseConfig } from './getBaseConfig';

export default defineConfig(options => [...getBaseConfig('browser', ['cjs', 'esm'], options)]);


