src/shared/RemainingAccounts.ts
===============================

Last edited: 2023-08-04 12:58:33

Contents:

.. code-block:: ts

    import { ImportFrom } from './ImportFrom';
import { mainCase } from './utils';

export type RemainingAccounts =
  | { kind: 'arg'; name: string; isWritable: boolean }
  | { kind: 'resolver'; name: string; importFrom: ImportFrom };

export const remainingAccountsFromArg = (
  arg: string,
  isWritable: boolean = false
): RemainingAccounts => ({ kind: 'arg', name: mainCase(arg), isWritable });

export const remainingAccountsFromResolver = (
  name: string,
  importFrom: ImportFrom = 'hooked'
): RemainingAccounts => ({
  kind: 'resolver',
  name: mainCase(name),
  importFrom,
});


