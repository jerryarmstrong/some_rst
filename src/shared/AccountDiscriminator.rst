src/shared/AccountDiscriminator.ts
==================================

Last edited: 2023-08-04 12:58:33

Contents:

.. code-block:: ts

    import { mainCase } from './utils';

export type AccountDiscriminator =
  | { kind: 'field'; name: string }
  | { kind: 'size' };

export const fieldAccountDiscriminator = (
  name: string
): AccountDiscriminator => ({ kind: 'field', name: mainCase(name) });

export const sizeAccountDiscriminator = (): AccountDiscriminator => ({
  kind: 'size',
});


