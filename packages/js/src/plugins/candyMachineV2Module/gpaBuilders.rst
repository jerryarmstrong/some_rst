packages/js/src/plugins/candyMachineV2Module/gpaBuilders.ts
===========================================================

Last edited: 2023-05-26 09:49:40

Contents:

.. code-block:: ts

    import { PublicKey } from '@solana/web3.js';
import { GpaBuilder } from '@/utils';

type AccountDiscriminator = [
  number,
  number,
  number,
  number,
  number,
  number,
  number,
  number
];
// TODO(thlorenz): copied from candy machine SDK
// SDK should either provide a GPA builder or expose this discriminator
const candyMachineV2Discriminator: AccountDiscriminator = [
  51, 173, 177, 113, 25, 241, 109, 189,
];

const AUTHORITY = candyMachineV2Discriminator.length;
const WALLET = AUTHORITY + PublicKey.default.toBytes().byteLength;

export class CandyMachineV2GpaBuilder extends GpaBuilder {
  whereDiscriminator(discrimator: AccountDiscriminator) {
    return this.where(0, Buffer.from(discrimator));
  }

  candyMachineAccounts() {
    return this.whereDiscriminator(candyMachineV2Discriminator);
  }

  // wallet same as solTreasury
  candyMachineAccountsForWallet(wallet: PublicKey) {
    return this.candyMachineAccounts().where(WALLET, wallet.toBase58());
  }

  candyMachineAccountsForAuthority(authority: PublicKey) {
    return this.candyMachineAccounts().where(AUTHORITY, authority.toBase58());
  }
}


