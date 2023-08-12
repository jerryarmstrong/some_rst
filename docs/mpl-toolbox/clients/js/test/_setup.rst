clients/js/test/_setup.ts
=========================

Last edited: 2023-06-19 17:40:55

Contents:

.. code-block:: ts

    /* eslint-disable import/no-extraneous-dependencies */
import {
  generateSigner,
  Option,
  PublicKey,
  Signer,
  transactionBuilder,
  Umi,
} from '@metaplex-foundation/umi';
import { createUmi as basecreateUmi } from '@metaplex-foundation/umi-bundle-tests';
import {
  createMint as baseCreateMint,
  createToken as baseCreateToken,
  mintTokensTo,
  mplToolbox,
} from '../src';

export const createUmi = async () => (await basecreateUmi()).use(mplToolbox());

export const createMint = async (
  umi: Umi,
  input: {
    decimals?: number;
    mintAuthority?: PublicKey;
    freezeAuthority?: Option<PublicKey>;
  } = {}
): Promise<Signer> => {
  const mint = generateSigner(umi);
  await baseCreateMint(umi, { mint, ...input }).sendAndConfirm(umi);
  return mint;
};

export const createToken = async (
  umi: Umi,
  input: {
    mint: PublicKey;
    amount?: number | bigint;
    owner?: PublicKey;
    mintAuthority?: Signer;
  }
): Promise<Signer> => {
  const token = generateSigner(umi);
  let builder = transactionBuilder().add(
    baseCreateToken(umi, {
      token,
      mint: input.mint,
      owner: input.owner,
    })
  );
  if (input.amount) {
    builder = builder.add(
      mintTokensTo(umi, {
        mint: input.mint,
        mintAuthority: input.mintAuthority,
        token: token.publicKey,
        amount: input.amount,
      })
    );
  }
  await builder.sendAndConfirm(umi);
  return token;
};

export const createMintAndToken = async (
  umi: Umi,
  input: {
    decimals?: number;
    mintAuthority?: Signer;
    freezeAuthority?: Option<PublicKey>;
    owner?: PublicKey;
    amount?: number | bigint;
  } = {}
): Promise<[Signer, Signer]> => {
  const mint = await createMint(umi, {
    decimals: input.decimals,
    mintAuthority: input.mintAuthority?.publicKey,
    freezeAuthority: input.freezeAuthority,
  });
  const token = await createToken(umi, {
    mint: mint.publicKey,
    amount: input.amount,
    owner: input.owner,
    mintAuthority: input.mintAuthority,
  });
  return [mint, token];
};


