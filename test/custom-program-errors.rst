test/custom-program-errors.ts
=============================

Last edited: 2021-12-28 22:07:55

Contents:

.. code-block:: ts

    import test from 'tape'
import { CustomProgramError, initCusper } from '../src/resolve-error'
import { strict as assert } from 'assert'

const penMsg = `Numbers I've got by the dozen | Everyone's uncle and cousin | But I can't live without buzzin' | Pennsylvania Six, Five Thousand `
const cusper = initCusper((code: number) => {
  switch (code) {
    case 65000: {
      const err = new CustomProgramError(code, 'Pensylvania 6-5000', penMsg)
      return err
    }
  }
})

test('resolving custom error', (t) => {
  const err = cusper.errorFromCode(65000)
  assert(err != null, 'finds the error')

  t.equal(err.code, 65000, 'resolves correct error')
  t.equal(err.message, penMsg, 'includes error message')
  t.equal(
    err.name,
    'CustomProgramError#Pensylvania 6-5000',
    'includes correct name'
  )
  t.end()
})


