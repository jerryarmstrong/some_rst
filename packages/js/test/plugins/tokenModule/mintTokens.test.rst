packages/js/test/plugins/tokenModule/mintTokens.test.ts
=======================================================

Last edited: 2023-05-26 09:49:40

Contents:

.. code-block:: ts

    import { Keypair } from '@solana/web3.js';
import test, { Test } from 'tape';
import { killStuckProcess, metaplex } from '../../helpers';
import { assertRefreshedTokenHasAmount, assertTokenHasAmount } from './helpers';
import { token } from '@/index';

killStuckProcess();

test('[tokenModule] it can mint tokens to an existing token account', async (t: Test) => {
  // Given a Metaplex instance and a mint.
  const mx = await metaplex();
  const { mint } = await mx.tokens().createMint();

  // And an existing token account for that mint.
  const toTokenSigner = Keypair.generate();
  const { token: toToken } = await mx
    .tokens()
    .createToken({ mint: mint.address, token: toTokenSigner });

  assertTokenHasAmount(t, toToken, token(0));

  // When we mint 42 tokens to that token account.
  await mx.tokens().mint({
    mintAddress: mint.address,
    amount: token(42),
    toToken: toToken.address,
  });

  // Then the mint was successful.
  await assertRefreshedTokenHasAmount(t, mx, toToken, token(42));
});

test('[tokenModule] it can mint tokens to an existing associated token account', async (t: Test) => {
  // Given a Metaplex instance and a mint.
  const mx = await metaplex();
  const { mint } = await mx.tokens().createMint();

  // And an existing associated token account for that mint.
  const toOwner = Keypair.generate().publicKey;
  const { token: toToken } = await mx
    .tokens()
    .createToken({ mint: mint.address, owner: toOwner });

  assertTokenHasAmount(t, toToken, token(0));

  // When we mint 42 tokens to that token account.
  await mx.tokens().mint({
    mintAddress: mint.address,
    amount: token(42),
    toToken: toToken.address,
  });

  // Then the mint was successful.
  await assertRefreshedTokenHasAmount(t, mx, toToken, token(42));
});

test('[tokenModule] it can mint tokens to an non-existing token account', async (t: Test) => {
  // Given a Metaplex instance and a mint.
  const mx = await metaplex();
  const { mint } = await mx.tokens().createMint();

  // And an token account to send tokens to that does not exist.
  const toTokenSigner = Keypair.generate();
  const toTokenAccount = await mx.rpc().getAccount(toTokenSigner.publicKey);
  t.false(toTokenAccount.exists, 'toToken account does not exist');

  // When we mint 42 tokens to that token account.
  await mx.tokens().mint({
    mintAddress: mint.address,
    amount: token(42),
    toToken: toTokenSigner,
  });

  // Then the account was created.
  const toToken = await mx
    .tokens()
    .findTokenByAddress({ address: toTokenSigner.publicKey });

  // And the mint was successful.
  await assertRefreshedTokenHasAmount(t, mx, toToken, token(42));
});

test('[tokenModule] it can mint tokens to an non-existing associated token account', async (t: Test) => {
  // Given a Metaplex instance and a mint.
  const mx = await metaplex();
  const { mint } = await mx.tokens().createMint();

  // And an owner that does not have an associated token account for that mint yet.
  const toOwner = Keypair.generate().publicKey;
  const toAssociatedToken = mx.tokens().pdas().associatedTokenAccount({
    mint: mint.address,
    owner: toOwner,
  });
  const toAssociatedTokenAccount = await mx.rpc().getAccount(toAssociatedToken);
  t.false(toAssociatedTokenAccount.exists, 'toToken account does not exist');

  // When we mint 42 tokens to that token account.
  await mx
    .tokens()
    .mint({ mintAddress: mint.address, amount: token(42), toOwner });

  // Then the associated token account was created.
  const toToken = await mx
    .tokens()
    .findTokenByAddress({ address: toAssociatedToken });

  // And the mint was successful.
  await assertRefreshedTokenHasAmount(t, mx, toToken, token(42));
});


