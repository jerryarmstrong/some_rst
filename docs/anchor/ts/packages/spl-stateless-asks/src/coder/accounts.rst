ts/packages/spl-stateless-asks/src/coder/accounts.ts
====================================================

Last edited: 2022-12-14 20:15:57

Contents:

.. code-block:: ts

    // @ts-nocheck
import * as B from "@native-to-anchor/buffer-layout";
import { AccountsCoder, Idl } from "@project-serum/anchor";
import { IdlTypeDef } from "@project-serum/anchor/dist/cjs/idl";

export class SplStatelessAsksAccountsCoder<A extends string = string>
  implements AccountsCoder
{
  constructor(_idl: Idl) {}

  public async encode<T = any>(accountName: A, account: T): Promise<Buffer> {
    switch (accountName) {
      default: {
        throw new Error(`Invalid account name: ${accountName}`);
      }
    }
  }

  public decode<T = any>(accountName: A, ix: Buffer): T {
    return this.decodeUnchecked(accountName, ix);
  }

  public decodeUnchecked<T = any>(accountName: A, ix: Buffer): T {
    switch (accountName) {
      default: {
        throw new Error(`Invalid account name: ${accountName}`);
      }
    }
  }

  public memcmp(
    accountName: A,
    _appendData?: Buffer
  ): { dataSize?: number; offset?: number; bytes?: string } {
    switch (accountName) {
      default: {
        throw new Error(`Invalid account name: ${accountName}`);
      }
    }
  }

  public size(idlAccount: IdlTypeDef): number {
    switch (idlAccount.name) {
      default: {
        throw new Error(`Invalid account name: ${idlAccount.name}`);
      }
    }
  }
}


