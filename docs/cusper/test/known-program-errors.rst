test/known-program-errors.ts
============================

Last edited: 2021-12-28 22:07:55

Contents:

.. code-block:: ts

    import test from 'tape'
import * as anchor from '../src/errors/anchor'
import { tokenLendingErrors } from '../src/errors/token-lending'
import { initCusper } from '../src/resolve-error'
import { strict as assert } from 'assert'
import { ErrorWithLogs } from '../src/types'

const cusper = initCusper()

// -----------------
// Anchor
// -----------------
test('resolving anchor error', (t) => {
  const err = cusper.errorFromCode(anchor.LangErrorCode.ConstraintSeeds)
  assert(err != null, 'finds the error')
  t.equal(
    err.code,
    anchor.LangErrorCode.ConstraintSeeds,
    'resolves correct error'
  )
  t.equal(
    err.message,
    anchor.LangErrorMessage.get(err.code),
    'includes error message'
  )
  t.equal(err.name, 'AnchorError#ConstraintSeeds', 'includes correct name')
  t.end()
})

test('throwing anchor error', (t) => {
  const logs = [
    'Program CwrqeMj2U8tFr1Rhkgwc84tpAsqbt9pTt2a4taoTADPr invoke [1]',
    'Program log: Custom program error: 0x07D0',
  ]
  try {
    const error: ErrorWithLogs = { ...new Error('Test error'), logs }
    cusper.throwError(error)
    t.fail('should throw error')
  } catch (err: any) {
    assert(err != null, 'finds the error')
    t.equal(
      err.code,
      anchor.LangErrorCode.ConstraintMut,
      'throws correct error'
    )
    t.equal(
      err.message,
      anchor.LangErrorMessage.get(err.code),
      'includes error message'
    )
    t.equal(err.name, 'AnchorError#ConstraintMut', 'includes correct name')
  }
  t.end()
})

// -----------------
// Token Lending
// -----------------
test('resolving token lending error', (t) => {
  const code = 2
  const tokenLendingError = tokenLendingErrors.get(code)!
  const err = cusper.errorFromCode(code)
  assert(err != null, 'finds the error')
  t.equal(err.code, code, 'resolves correct error')
  t.equal(err.message, tokenLendingError.message, 'includes error message')
  t.equal(err.name, 'TokenLendingError#NotRentExempt', 'includes correct name')
  t.end()
})


