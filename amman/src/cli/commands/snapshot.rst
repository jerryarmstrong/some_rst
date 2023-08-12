amman/src/cli/commands/snapshot.ts
==================================

Last edited: 2022-11-03 12:19:53

Contents:

.. code-block:: ts

    import { cliAmmanInstance } from '../utils'

export async function handleSnapshotCommand(label?: string) {
  const amman = cliAmmanInstance()
  const snapshotDir = await amman.ammanClient.requestSnapshot(label)

  amman.disconnect()

  return snapshotDir
}


