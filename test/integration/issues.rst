test/integration/issues.ts
==========================

Last edited: 2023-07-06 15:09:22

Contents:

.. code-block:: ts

    import { Idl } from '../../src/solita'
import test from 'tape'
import { checkIdl } from '../utils/check-idl'

import emptyAccountsJson from './fixtures/issue-empty-accounts.json'
import missingBeetImportJson from './fixtures/issue-missing-beet-import.json'

// -----------------
// issue-empty-accounts
// -----------------
{
  const label = 'issue-empty-accounts'

  test('renders type correct SDK for ' + label, async (t) => {
    const idl = emptyAccountsJson as Idl
    await checkIdl(t, idl, label)
  })
}
// -----------------
// issue-missing-beet-import
// -----------------
{
  const label = 'issue-missing-beet-import'

  test('renders type correct SDK for ' + label, async (t) => {
    const idl = missingBeetImportJson as Idl
    await checkIdl(t, idl, label)
  })
}


