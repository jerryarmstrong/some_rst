token-lending/js/rollup.config.ts
=================================

Last edited: 2022-07-07 18:10:20

Contents:

.. code-block:: ts

    import commonjs from '@rollup/plugin-commonjs';
import nodeResolve from '@rollup/plugin-node-resolve';
import typescript from '@rollup/plugin-typescript';
import pkg from './package.json';

export default {
    input: 'src/index.ts',
    output: [
        { file: pkg.main, format: 'cjs', sourcemap: true },
        { file: pkg.module, format: 'es', sourcemap: true },
    ],
    external: ['@solana/spl-token', '@solana/web3.js', 'assert', 'buffer', 'fs', 'path'],
    watch: {
        include: 'src/**',
    },
    plugins: [typescript(), commonjs(), nodeResolve()],
};


