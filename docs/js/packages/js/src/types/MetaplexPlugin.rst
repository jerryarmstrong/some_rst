packages/js/src/types/MetaplexPlugin.ts
=======================================

Last edited: 2023-05-26 09:49:40

Contents:

.. code-block:: ts

    import type { Metaplex } from '@/Metaplex';

export type MetaplexPlugin = {
  install(metaplex: Metaplex): void;
};


