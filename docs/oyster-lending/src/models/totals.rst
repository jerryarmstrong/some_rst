src/models/totals.ts
====================

Last edited: 2021-03-16 20:45:52

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


