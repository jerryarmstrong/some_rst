src/utils/parse-cargo-toml.ts
=============================

Last edited: 2023-08-11 16:30:29

Contents:

.. code-block:: ts

    import { promises as fs } from 'fs'
import { logError } from './log'
import { parse } from 'toml'

/** @private */
export type CargoToml = {
  dependencies: Record<string, string | { version: string }>
}

/** @private */
export async function parseCargoToml(fullPath: string) {
  let toml
  try {
    toml = await fs.readFile(fullPath, 'utf8')
  } catch (err) {
    logError('Failed to read Cargo.toml at "%s"\n', fullPath, err)
    throw err
  }
  try {
    const parsed: CargoToml = parse(toml)
    return { parsed, toml }
  } catch (err) {
    logError('Failed to parse Cargo.toml:\n%s\n%s', toml, err)
    throw err
  }
}


