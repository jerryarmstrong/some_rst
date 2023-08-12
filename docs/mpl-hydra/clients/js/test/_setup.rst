clients/js/test/_setup.ts
=========================

Last edited: 2023-06-19 18:36:17

Contents:

.. code-block:: ts

    /* eslint-disable import/no-extraneous-dependencies */
import { createUmi as baseCreateUmi } from '@metaplex-foundation/umi-bundle-tests';
import { mplHydra } from '../src';

export const createUmi = async () => (await baseCreateUmi()).use(mplHydra());


