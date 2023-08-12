js/packages/web/src/models/totals.ts
====================================

Last edited: 2022-06-29 06:18:54

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


