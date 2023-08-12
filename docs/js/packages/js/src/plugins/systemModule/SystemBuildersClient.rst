packages/js/src/plugins/systemModule/SystemBuildersClient.ts
============================================================

Last edited: 2023-05-26 09:49:40

Contents:

.. code-block:: ts

    import {
  createAccountBuilder,
  CreateAccountBuilderParams,
  transferSolBuilder,
  TransferSolBuilderParams,
} from './operations';
import type { Metaplex } from '@/Metaplex';
import { TransactionBuilderOptions } from '@/utils';

/**
 * This client allows you to access the underlying Transaction Builders
 * for the write operations of the System module.
 *
 * @see {@link SystemClient}
 * @group Module Builders
 * */
export class SystemBuildersClient {
  constructor(protected readonly metaplex: Metaplex) {}

  /** {@inheritDoc createAccountBuilder} */
  createAccount(
    input: CreateAccountBuilderParams,
    options?: TransactionBuilderOptions
  ) {
    return createAccountBuilder(this.metaplex, input, options);
  }

  /** {@inheritDoc transferSolBuilder} */
  transferSol(
    input: TransferSolBuilderParams,
    options?: TransactionBuilderOptions
  ) {
    return transferSolBuilder(this.metaplex, input, options);
  }
}


