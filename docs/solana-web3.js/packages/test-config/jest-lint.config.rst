packages/test-config/jest-lint.config.ts
========================================

Last edited: 2023-08-11 09:49:26

Contents:

.. code-block:: ts

    import type { Config } from '@jest/types';

const config: Partial<Config.InitialProjectOptions> = {
    displayName: {
        color: 'cyanBright',
        name: 'ESLint',
    },
    runner: 'eslint',
    testMatch: ['<rootDir>src/**/*.ts'],
};

export default config;


