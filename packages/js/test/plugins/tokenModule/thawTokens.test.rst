packages/js/test/plugins/tokenModule/thawTokens.test.ts
=======================================================

Last edited: 2023-05-26 09:49:40

Contents:

.. code-block:: ts

    import { AccountState } from '@solana/spl-token';
import { Keypair } from '@solana/web3.js';
import test, { Test } from 'tape';
import { killStuckProcess, metaplex } from '../../helpers';
import { refreshToken } from './helpers';

killStuckProcess();

test('[tokenModule] the freeze authority can thaw any frozen token account', async (t: Test) => {
  // Given a Metaplex instance and an existing token account.
  const mx = await metaplex();
  const freezeAuthority = Keypair.generate();
  const owner = Keypair.generate();
  const { token: tokenWithMint } = await mx.tokens().createTokenWithMint({
    owner: owner.publicKey,
    freezeAuthority: freezeAuthority.publicKey,
  });

  // And given that account has been frozen.
  await mx.tokens().freeze({
    mintAddress: tokenWithMint.mint.address,
    tokenOwner: owner.publicKey,
    freezeAuthority,
  });

  // When the freeze authority thaws the account.
  await mx.tokens().thaw({
    mintAddress: tokenWithMint.mint.address,
    tokenOwner: owner.publicKey,
    freezeAuthority,
  });

  // Then the token account is no longer frozen.
  const refreshedToken = await refreshToken(mx, tokenWithMint);
  t.equal(
    refreshedToken.state,
    AccountState.Initialized,
    'token account is not frozen'
  );
});


