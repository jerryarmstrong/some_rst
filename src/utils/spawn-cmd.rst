src/utils/spawn-cmd.ts
======================

Last edited: 2023-08-11 16:30:29

Contents:

.. code-block:: ts

    import { spawn, SpawnOptions } from 'child_process'
import { logDebug } from './log'

// error: could not find `anchor-cli` in registry `crates-io` with version `~0.22`
const installNotFoundRx = /could not find.+in registry/

/** @private */
export function spawnCmd(
  cmd: string,
  args: string[],
  options: SpawnOptions = {}
): Promise<void> {
  return new Promise<void>((resolve, reject) => {
    let rejected = false
    const child = spawn(cmd, args, options)

    child.stdout?.on('data', (buf) => {
      const msg = buf.toString()
      logDebug('spawnCmd stdout data', msg)
      logDebug('spawnCmd stdout regex', installNotFoundRx.test(msg))
      if (installNotFoundRx.test(msg)) {
        rejected = true
        child.kill()
        reject(new Error(msg))
      } else {
        process.stdout.write(buf)
      }
    })
    child.stderr?.on('data', (buf) => {
      const msg = buf.toString()
      logDebug('spawnCmd stderr data', msg)
      logDebug('spawnCmd stderr regex', installNotFoundRx.test(msg))
      if (installNotFoundRx.test(msg)) {
        rejected = true
        child.kill()
        reject(new Error(msg))
      } else {
        process.stderr.write(buf)
      }
    })

    child
      .on('error', (err) => {
        logDebug('spawnCmd error', err)
        rejected = true
        reject(err)
      })
      .on('exit', () => {
        logDebug('spawnCmd exit, rejected: ' + (rejected ? 'true' : 'false'))
        if (!rejected) resolve()
      })
  })
}


