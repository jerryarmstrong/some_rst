src/shared/BytesCreatedOnChain.ts
=================================

Last edited: 2023-08-04 12:58:33

Contents:

.. code-block:: ts

    import { ImportFrom } from './ImportFrom';
import { mainCase } from './utils';

export type BytesCreatedOnChain =
  | { kind: 'number'; value: number; includeHeader: boolean }
  | { kind: 'arg'; name: string; includeHeader: boolean }
  | {
      kind: 'account';
      name: string;
      importFrom: ImportFrom;
      includeHeader: boolean;
    }
  | { kind: 'resolver'; name: string; importFrom: ImportFrom };

export const bytesFromNumber = (
  value: number,
  includeHeader: boolean = true
): BytesCreatedOnChain => ({ kind: 'number', value, includeHeader });

export const bytesFromArg = (
  arg: string,
  includeHeader: boolean = true
): BytesCreatedOnChain => ({ kind: 'arg', name: mainCase(arg), includeHeader });

export const bytesFromAccount = (
  account: string,
  importFrom: ImportFrom = 'generated',
  includeHeader: boolean = true
): BytesCreatedOnChain => ({
  kind: 'account',
  name: mainCase(account),
  importFrom,
  includeHeader,
});

export const bytesFromResolver = (
  name: string,
  importFrom: ImportFrom = 'hooked'
): BytesCreatedOnChain => ({
  kind: 'resolver',
  name: mainCase(name),
  importFrom,
});


