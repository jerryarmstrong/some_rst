src/utils/version.ts
====================

Last edited: 2023-08-11 16:30:29

Contents:

.. code-block:: ts

    import { spawnSync } from 'child_process'
import satisfies from 'semver/functions/satisfies'
import { canAccess } from './fs'
import { logDebug, logError, logInfo } from './log'

/** @private */
export const versionRx =
  /([0-9]+\.[0-9]+\.[0-9]+)(?:-[0-9A-Za-z-]+(?:\.[0-9A-Za-z-]+)*)?(?:\+[0-9A-Za-z-]+)?/

/** @private */
export async function getBinaryVersion(
  fullPathToBinary: string,
  binaryVersionFlag: string,
  binaryVersionRx: RegExp
) {
  const versionCmd = `${fullPathToBinary} ${binaryVersionFlag}`
  const { stdout, stderr, error } = spawnSync(fullPathToBinary, [
    binaryVersionFlag,
  ])
  if (error) {
    logError(`Error running ${versionCmd}: ${error}`)
    throw error
  }
  const output = `${stdout.toString()}${stderr.toString()}`

  logDebug(`versionCmd: ${versionCmd} ->\n${output}`)
  const match = output.match(binaryVersionRx)
  return { binVersion: match == null ? undefined : match[0], output }
}

/** @private */
export async function binarySatisfies(
  fullPathToBinary: string,
  binaryVersionFlag: string,
  binaryVersionRx: RegExp,
  libVersionRange: string
) {
  if (!(await canAccess(fullPathToBinary))) {
    logInfo(
      `Cannot access ${fullPathToBinary} thus will need to install the first time`
    )
    return { binVersion: undefined, satisfies: false }
  }

  const { binVersion, output } = await getBinaryVersion(
    fullPathToBinary,
    binaryVersionFlag,
    binaryVersionRx
  )

  if (binVersion == null) {
    logError(`Unable to extract version from ${output} will require reinstall`)
    return { binVersion: undefined, satisfies: false }
  }
  return {
    binVersion,
    satisfies: satisfies(binVersion, libVersionRange),
  }
}

/** @private */
export function installArgs(
  binaryCrateName: string,
  libVersionRange: string,
  locked: boolean,
  rootDir: string
) {
  return [
    'install',
    binaryCrateName,
    '--version',
    libVersionRange,
    ...(locked ? ['--locked'] : []),
    '--force',
    '--root',
    rootDir,
  ]
}


