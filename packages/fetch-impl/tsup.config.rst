packages/fetch-impl/tsup.config.ts
==================================

Last edited: 2023-08-11 09:49:26

Contents:

.. code-block:: ts

    import { defineConfig } from 'tsup';

export default defineConfig(_options =>
    (['browser', 'node'] as const).map(platform => ({
        entry: [`./src/**`],
        format: ['cjs', 'esm'],
        minify: true,
        name: platform,
        platform,
        sourcemap: true,
        treeshake: true,
    }))
);


