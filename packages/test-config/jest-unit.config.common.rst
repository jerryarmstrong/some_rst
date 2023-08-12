packages/test-config/jest-unit.config.common.ts
===============================================

Last edited: 2023-08-11 09:49:26

Contents:

.. code-block:: ts

    import { Config } from '@jest/types';
import path from 'path';

const config: Partial<Config.InitialProjectOptions> = {
    restoreMocks: true,
    roots: ['<rootDir>/src/'],
    setupFilesAfterEnv: [
        path.resolve(__dirname, 'setup-dev-mode.ts'),
        path.resolve(__dirname, 'setup-define-version-constant.ts'),
        path.resolve(__dirname, 'setup-fetch-mock.ts'),
        path.resolve(__dirname, 'setup-webcrypto.ts'),
    ],
    transform: {
        '^.+\\.(ts|js)$': [
            '@swc/jest',
            {
                jsc: {
                    target: 'es2020',
                },
            },
        ],
    },
};

export default config;


