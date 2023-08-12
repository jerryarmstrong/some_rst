test/tools/validators/pubkey.test.ts
====================================

Last edited: 2023-08-11 18:13:34

Contents:

.. code-block:: ts

    import { tryParseDomain } from '@tools/validators/pubkey'

describe('Public Key Resolves ', () => {
  const domain = 'realms.sol'
  const pubkey = '8aHFSYp3K2X2qEfUqQhfCuCHvjDumdiMzfCyrJhdJxmQ'

  test('domains to publicKey', async () => {
    const resolvedKey = await tryParseDomain(domain)
    expect(resolvedKey?.toBase58()).toEqual(pubkey)
  })
})


