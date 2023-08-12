clients/js/test/_setup.ts
=========================

Last edited: 2023-07-13 14:48:42

Contents:

.. code-block:: ts

    /* eslint-disable import/no-extraneous-dependencies */
import { createUmi as basecreateUmi } from '@metaplex-foundation/umi-bundle-tests';
import { mplTrifle } from '../src';

export const createUmi = async () => (await basecreateUmi()).use(mplTrifle());


