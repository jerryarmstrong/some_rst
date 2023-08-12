amman/src/cli/commands/logs.ts
==============================

Last edited: 2022-11-03 12:19:53

Contents:

.. code-block:: ts

    import { maybeAmmanInstance } from '../utils'
import { pipeSolanaLogs } from '../utils/solana-logs'

export function handleLogsCommand() {
  return pipeSolanaLogs(maybeAmmanInstance())
}


