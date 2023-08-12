test/parse-error.ts
===================

Last edited: 2021-12-28 22:07:55

Contents:

.. code-block:: ts

    import test from 'tape'
import { errorCodeFromLogs } from '../src/parse-error'

test('parsing error logs with code', (t) => {
  const logs = [
    'Program CwrqeMj2U8tFr1Rhkgwc84tpAsqbt9pTt2a4taoTADPr invoke [1]',
    'Program log: Instruction: Increment',
    'Program log: Custom program error: 0x1771',
    'Program CwrqeMj2U8tFr1Rhkgwc84tpAsqbt9pTt2a4taoTADPr consumed 3240 of 200000 compute units',
    'Program CwrqeMj2U8tFr1Rhkgwc84tpAsqbt9pTt2a4taoTADPr failed: custom program error: 0x1771',
  ]

  const code = errorCodeFromLogs(logs)
  t.equal(code, 0x1771, 'returns correct code')
  t.end()
})

test('parsing error logs without code', (t) => {
  const logs = [
    'Program CwrqeMj2U8tFr1Rhkgwc84tpAsqbt9pTt2a4taoTADPr invoke [1]',
    'Program log: Instruction: Increment',
    'Program CwrqeMj2U8tFr1Rhkgwc84tpAsqbt9pTt2a4taoTADPr consumed 3240 of 200000 compute units',
  ]

  const code = errorCodeFromLogs(logs)
  t.notOk(code, 'returns null')
  t.end()
})


