packages/lending/src/models/totals.ts
=====================================

Last edited: 2023-07-19 16:40:40

Contents:

.. code-block:: ts

    export interface TotalItem {
  key: string;
  marketSize: number;
  borrowed: number;
  name: string;
}

export interface Totals {
  marketSize: number;
  borrowed: number;
  lentOutPct: number;
  items: TotalItem[];
}


