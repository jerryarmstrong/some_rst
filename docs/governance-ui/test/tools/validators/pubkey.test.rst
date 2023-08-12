test/tools/validators/pubkey.test.ts
====================================

Last edited: 2023-05-19 22:20:18

Contents:

.. code-block:: ts

    import { tryParseDomain } from '@tools/validators/pubkey'

describe('Public Key Resolves ', () => {
  const domain = 'realms.sol'
  const pubkey = '33m47vH6Eav6jr5Ry86XjhRft2jRBLDnDgPSHoquXi2Z'

  test('domains to publicKey', async () => {
    const resolvedKey = await tryParseDomain(domain)
    expect(resolvedKey?.toBase58()).toEqual(pubkey)
  })
})


