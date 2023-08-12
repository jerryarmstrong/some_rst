src/visitors/workers/ConsoleLogVisitor.ts
=========================================

Last edited: 2023-08-04 12:58:33

Contents:

.. code-block:: ts

    import { BaseDelegateVisitor } from '../BaseDelegateVisitor';

export class ConsoleLogVisitor extends BaseDelegateVisitor<any, void> {
  map(value: any): void {
    // eslint-disable-next-line no-console
    console.log(value);
  }
}


