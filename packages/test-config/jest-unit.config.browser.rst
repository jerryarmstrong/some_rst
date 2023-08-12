packages/test-config/jest-unit.config.browser.ts
================================================

Last edited: 2023-08-11 09:49:26

Contents:

.. code-block:: ts

    import type { Config } from '@jest/types';
import path from 'path';

import commonConfig from './jest-unit.config.common';

const config: Partial<Config.InitialProjectOptions> = {
    ...commonConfig,
    displayName: {
        color: 'grey',
        name: 'Unit Test (Browser)',
    },
    globals: {
        ...commonConfig.globals,
        __BROWSER__: true,
        __NODEJS__: false,
        __REACTNATIVE__: false,
    },
    setupFilesAfterEnv: [
        ...(commonConfig.setupFilesAfterEnv ?? []),
        path.resolve(__dirname, 'setup-secure-context.ts'),
        path.resolve(__dirname, 'setup-text-encoder.ts'),
    ],
    testEnvironment: 'jsdom',
    testEnvironmentOptions: {},
};

export default config;


