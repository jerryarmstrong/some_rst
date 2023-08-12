packages/test-config/jest-dev.config.ts
=======================================

Last edited: 2023-08-11 09:49:26

Contents:

.. code-block:: ts

    import type { Config } from 'jest';
import path from 'path';

const config: Config = {
    projects: [
        path.resolve(__dirname, 'jest-lint.config.ts'),
        path.resolve(__dirname, 'jest-prettier.config.ts'),
        path.resolve(__dirname, 'jest-unit.config.browser.ts'),
        path.resolve(__dirname, 'jest-unit.config.node.ts'),
    ],
    watchPlugins: [
        'jest-watch-master',
        'jest-watch-select-projects',
        'jest-watch-typeahead/filename',
        'jest-watch-typeahead/testname',
    ],
    workerThreads: true,
};

export default config;


