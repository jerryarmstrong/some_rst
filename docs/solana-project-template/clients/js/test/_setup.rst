clients/js/test/_setup.ts
=========================

Last edited: 2023-07-16 23:08:25

Contents:

.. code-block:: ts

    /* eslint-disable import/no-extraneous-dependencies */
import { createUmi as basecreateUmi } from '@metaplex-foundation/umi-bundle-tests';
import { mplProjectName } from '../src';

export const createUmi = async () =>
  (await basecreateUmi()).use(mplProjectName());


