packages/test-config/jest-unit.config.node.ts
=============================================

Last edited: 2023-08-11 09:49:26

Contents:

.. code-block:: ts

    import { Config } from '@jest/types';

import commonConfig from './jest-unit.config.common';

const config: Partial<Config.InitialProjectOptions> = {
    ...commonConfig,
    displayName: {
        color: 'grey',
        name: 'Unit Test (Node)',
    },
    globals: {
        ...commonConfig.globals,
        __BROWSER__: false,
        __NODEJS__: true,
        __REACTNATIVE__: false,
    },
};

export default config;


