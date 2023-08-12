src/utils/confirm.ts
====================

Last edited: 2023-08-11 16:30:29

Contents:

.. code-block:: ts

    /**
 * The args passed to {@link ConfirmInstall}
 */
export type ConfirmInstallArgs = {
  binaryName: string
  libName: string
  libVersion: string
  binVersion?: string
  fullPathToBinary: string
}

/**
 * Function that can be passed to {@link rustbinMatch} to confirm the install
 * step.
 *
 * Return `true` if it should be installed and `false` if not.
 *
 * This can also be used to print information about the install about to happen.
 */
export type ConfirmInstall = (args: ConfirmInstallArgs) => Promise<boolean>

/**
 * Prints information about the install about to happen to the console and
 * confirms it.
 */
export function confirmAutoMessageConsole({
  binaryName,
  libVersion,
  libName,
  binVersion,
  fullPathToBinary,
}: ConfirmInstallArgs) {
  if (binVersion == null) {
    console.error(`No existing version found for ${binaryName}.`)
  } else {
    console.error(`Version for ${binaryName}: ${binVersion}`)
  }
  console.error(
    `Will install version matching "${libName}: '${libVersion}'" to ${fullPathToBinary}`
  )
  return Promise.resolve(true)
}


