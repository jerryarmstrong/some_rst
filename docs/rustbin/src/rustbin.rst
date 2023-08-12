src/rustbin.ts
==============

Last edited: 2023-08-11 16:30:29

Contents:

.. code-block:: ts

    import path from 'path'
import {
  binarySatisfies,
  ConfirmInstall,
  getBinaryVersion,
  installArgs,
  logDebug,
  logError,
  logInfo,
  parseCargoToml,
  spawnCmd,
  versionRx,
} from './utils'
import table from 'text-table'

export * from './utils/confirm'

const DEFAULT_BINARY_VERSION_FLAG = '--version'

/** @private */
class Rustbin {
  readonly fullPathToBinary: string
  private constructor(
    readonly rootDir: string,
    readonly binaryName: string,
    readonly binaryCrateName: string,
    readonly binaryVersionFlag: string,
    readonly binaryVersionRx: RegExp,
    readonly libName: string,
    readonly cargoToml: string,
    readonly dryRun: boolean,
    readonly locked: boolean,
    readonly versionRangeFallback?: string
  ) {
    this.fullPathToBinary = path.join(rootDir, 'bin', binaryName)
    logDebug(this)
  }

  async check(): Promise<RustbinCheckReturn> {
    const libVersion = await this.getVersionInToml()
    const { binVersion, satisfies } = await binarySatisfies(
      this.fullPathToBinary,
      this.binaryVersionFlag,
      this.binaryVersionRx,
      libVersion
    )
    const rows = [
      ['Type', 'Name', 'Version'],
      ['----', '----', '-------'],
      ['lib', this.libName, libVersion],
      ['bin', this.binaryName, binVersion ?? '<unknown'],
    ]
    logInfo(table(rows))

    return {
      satisfies,
      libVersion,
      binVersion,
    }
  }

  private async getVersionInToml() {
    const { parsed, toml } = await parseCargoToml(this.cargoToml)
    const libVersion = parsed.dependencies[this.libName]
    if (libVersion == null) {
      logDebug(toml)
      throw new Error(
        `${this.libName} not found as dependency in ${this.cargoToml}`
      )
    }
    return typeof libVersion === 'string' ? libVersion : libVersion.version
  }

  async installMatchinBin(libVersionRange: string) {
    // cargo install anchor-cli --version 0.24.2 --force --root `pwd`/scripts
    const cmd = 'cargo'
    const args = installArgs(
      this.binaryCrateName,
      libVersionRange,
      this.locked,
      this.rootDir
    )
    const fullCmd = `${cmd} ${args.join(' ')}`
    logInfo(fullCmd)
    if (!this.dryRun) {
      try {
        await spawnCmd(cmd, args)
      } catch (err: any) {
        const backupCmd = await this.handleFailedInstall(cmd, err)
        return backupCmd ?? fullCmd
      }
    }

    return fullCmd
  }

  async handleFailedInstall(cmd: string, err: any) {
    if (this.versionRangeFallback == null) {
      throw err
    } else {
      // NOTE: this fallback logic isn't tested as it would be a lot of setup to simulate
      logError(err.message)

      // 1. see if the currently installed binary matches the fallback
      const { satisfies } = await binarySatisfies(
        this.fullPathToBinary,
        this.binaryVersionFlag,
        this.binaryVersionRx,
        this.versionRangeFallback
      )
      if (satisfies) {
        logError(
          `Install for compatible version failed, using already installed fallback: '${this.versionRangeFallback}'`
        )
        return
      }

      // 2. if not, install it
      const args = installArgs(
        this.binaryCrateName,
        this.versionRangeFallback,
        this.locked,
        this.rootDir
      )
      const fullCmd = `${cmd} ${args.join(' ')}`
      logError(
        `Install for compatible version failed, trying fallback: '${this.versionRangeFallback}'`
      )
      logInfo(fullCmd)
      await spawnCmd(cmd, args)
      return fullCmd
    }
  }

  static fromConfig(config: RustbinConfig) {
    const {
      rootDir,
      binaryName,
      libName,
      binaryVersionRx = versionRx,
      binaryVersionFlag = DEFAULT_BINARY_VERSION_FLAG,
      dryRun = false,
      locked = false,
      cargoToml,
      versionRangeFallback,
    } = config
    const { binaryCrateName = binaryName } = config
    const fullRootDir = path.resolve(rootDir)
    const fullCargoToml = path.resolve(cargoToml)
    return new Rustbin(
      fullRootDir,
      binaryName,
      binaryCrateName,
      binaryVersionFlag,
      binaryVersionRx,
      libName,
      fullCargoToml,
      dryRun,
      locked,
      versionRangeFallback
    )
  }
}

/**
 * Returned by {@link rustbinCheck}
 *
 * @property satisfies - true if the binary version satisfies the library
 * version range
 * @property libVersion - the library version range
 * @property binVersion - the binary version (if it is not defined then the
 * binary was either not found or the version output could not be parsed)
 */
export type RustbinCheckReturn = {
  satisfies: boolean
  libVersion: string
  binVersion?: string
}

/**
 * Returned by {@link rustbinMatch}
 *
 * @property cmd - the command to install the binary (empty if no install is
 * needed)
 * @property libVersion - the library version range
 * @property binVersion - the binary version (if it is not defined then the
 * binary was either not found or the version output could not be parsed)
 * @property fullPathToBinary - the full path to the installed binary
 */
export type RustbinMatchReturn = {
  cmd?: string
  libVersion: string
  binVersion?: string
  fullPathToBinary: string
}

/**
 * Configures how rustbin checks/matches the installed binary
 * with the installed library.
 *
 * @property rootDir - the directory where `cargo install` will place the install metadata files and the binary below
 * `./bin`
 * @property binaryName - the name of the binary executable to check/install
 * @property binaryCrateName - the name of the binary on crates.io
 * @property binaryVersionFlag - the flag to pass to the binary to have it print the version string
 * @property binaryVersionRx - a regex to extract the version from the binary version output string
 * @property libName - the name of the matching installed library
 * @property cargoToml - the path to the Cargo.toml file in which the version of the library is defined
 * @property versionRangeFallback - the binary version/range to use if the one
 * matching the lib version is not installable. This should be used with care
 * as this could result in an incompatible version to be installed.
 * @property locked - if `true` a `--locked` flag is passed to `cargo install`
 * @property dryRun - if true, the binary will not be installed even if it is necessary
 */
export type RustbinConfig = {
  rootDir: string
  binaryName: string
  binaryCrateName?: string
  binaryVersionFlag?: string
  binaryVersionRx?: RegExp
  libName: string
  versionRangeFallback?: string
  cargoToml: string
  locked?: boolean
  dryRun?: boolean
}

/**
 * Queries version of the installed binary.
 *
 * @returns version of the installed binary or `undefined` if the binary was
 * not found or the version string could not be parsed
 */
export async function rustbinVersion(
  fullPathToBinary: string,
  binaryVersionFlag: string = DEFAULT_BINARY_VERSION_FLAG,
  binaryVersionRx: RegExp = versionRx
) {
  const { binVersion } = await getBinaryVersion(
    fullPathToBinary,
    binaryVersionFlag,
    binaryVersionRx
  )
  return binVersion
}

/**
 * Checks if the installed binary matches the installed library.
 *
 * @returns result of check including if the binary version satisfies the
 * library version range
 */
export function rustbinCheck(
  config: RustbinConfig
): Promise<RustbinCheckReturn> {
  const rustbin = Rustbin.fromConfig(config)
  return rustbin.check()
}

/**
 * Checks if the installed binary matches the installed library.
 * If not it attempts to install the latest binary matching the library version
 * range via `cargo install`.
 *
 * @returns result including the `cmd` used to install the binary (if it was
 * necessary), the full path to said binary and the installed version of it
 */
export async function rustbinMatch(
  config: RustbinConfig,
  confirmInstall: ConfirmInstall = () => Promise.resolve(true)
): Promise<RustbinMatchReturn> {
  const rustbin = Rustbin.fromConfig(config)
  const { satisfies, libVersion, binVersion } = await rustbin.check()
  if (
    satisfies ||
    !(await confirmInstall({
      binaryName: rustbin.binaryName,
      libName: rustbin.libName,
      libVersion,
      binVersion,
      fullPathToBinary: rustbin.fullPathToBinary,
    }))
  ) {
    return {
      libVersion,
      binVersion,
      fullPathToBinary: rustbin.fullPathToBinary,
    }
  }

  logInfo(`Installing ${libVersion} compatible version of ${config.binaryName}`)
  const cmd = await rustbin.installMatchinBin(libVersion)
  const installedBinVersion = await rustbinVersion(rustbin.fullPathToBinary)
  return {
    cmd,
    libVersion,
    binVersion: installedBinVersion,
    fullPathToBinary: rustbin.fullPathToBinary,
  }
}


