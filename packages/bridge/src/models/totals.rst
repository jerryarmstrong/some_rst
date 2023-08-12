packages/bridge/src/models/totals.ts
====================================

Last edited: 2023-07-19 16:40:40

Contents:

.. code-block:: ts

    export interface TotalItem {
  key: string;
  marketSize: number;
  nativeSize: number;
  name: string;
}

export interface Totals {
  marketSize: number;
  numberOfAssets: number;
  items: TotalItem[];
}


