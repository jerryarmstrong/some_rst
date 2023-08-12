packages/test-config/jest-prettier.config.ts
============================================

Last edited: 2023-08-11 09:49:26

Contents:

.. code-block:: ts

    import type { Config } from '@jest/types';

const config: Partial<Config.InitialProjectOptions> = {
    displayName: {
        color: 'magentaBright',
        name: 'Prettier',
    },
    moduleFileExtensions: ['js', 'ts', 'json', 'md'],
    runner: 'prettier',
    testMatch: ['<rootDir>/src/**', '<rootDir>*'],
};

export default config;


