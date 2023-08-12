test/rustbin.ts
===============

Last edited: 2023-08-11 16:30:29

Contents:

.. code-block:: ts

    import path from 'path'
import test from 'tape'
import { RustbinConfig, rustbinCheck, rustbinMatch } from '../src/rustbin'

const fixtures = path.join(__dirname, 'fixtures')
const ah = path.join(fixtures, 'ah')
const ahProgram = path.join(ah, 'program')
const ahJs = path.join(ah, 'js')
const ahScriptsRoot = path.join(ahJs, 'scripts')
const ahCargoToml = path.join(ahProgram, 'Cargo.toml')

test('rustbin: checking anchor versions', async (t) => {
  const config: Omit<RustbinConfig, 'binaryName'> = {
    rootDir: ahScriptsRoot,
    libName: 'anchor-lang',
    cargoToml: ahCargoToml,
  }

  {
    const binaryName = 'anchor-0.19.0'
    const { satisfies, libVersion, binVersion } = await rustbinCheck({
      ...config,
      binaryName,
    })
    t.notOk(
      satisfies,
      `anchor v${binVersion} does not satisfy anchor-lang: ${libVersion}`
    )
  }
  {
    const binaryName = 'anchor-0.24.2'
    const { satisfies, libVersion, binVersion } = await rustbinCheck({
      ...config,
      binaryName,
    })
    t.ok(
      satisfies,
      `anchor v${binVersion} satisfies anchor-lang: ${libVersion}`
    )
  }
  {
    const binaryName = 'anchor-0.25.1'
    const { satisfies, libVersion, binVersion } = await rustbinCheck({
      ...config,
      binaryName,
    })
    t.notOk(
      satisfies,
      `anchor v${binVersion} does not satisfy anchor-lang: ${libVersion}`
    )
  }
  t.end()
})

test('rustbin: syncing anchor versions', async (t) => {
  const config: Omit<RustbinConfig, 'binaryName'> = {
    rootDir: ahScriptsRoot,
    libName: 'anchor-lang',
    cargoToml: ahCargoToml,
    dryRun: true,
  }

  {
    const binaryName = 'anchor-0.19.0'
    const { cmd } = await rustbinMatch({
      ...config,
      binaryName,
    })
    t.match(
      cmd!,
      /cargo install anchor-0.19.0 --version ~0.24.1 --force --root .+ah\/js\/scripts/
    )
  }

  {
    const binaryName = 'anchor-0.24.2'
    const { cmd } = await rustbinMatch({
      ...config,
      binaryName,
    })
    t.notOk(cmd, 'no command executed to sync to anchor-0.24.2')
  }

  {
    const binaryName = 'anchor-0.25.1'
    const { cmd } = await rustbinMatch({
      ...config,
      binaryName,
    })
    t.match(
      cmd!,
      /cargo install anchor-0.25.1 --version ~0.24.1 --force --root .+ah\/js\/scripts/
    )
  }
})

test('rustbin: syncing anchor version --locked', async (t) => {
  const config: Omit<RustbinConfig, 'binaryName'> = {
    rootDir: ahScriptsRoot,
    libName: 'anchor-lang',
    cargoToml: ahCargoToml,
    dryRun: true,
    locked: true,
  }

  {
    const binaryName = 'anchor-0.19.0'
    const { cmd } = await rustbinMatch({
      ...config,
      binaryName,
    })
    t.match(
      cmd!,
      /cargo install anchor-0.19.0 --version ~0.24.1 --locked --force --root .+ah\/js\/scripts/
    )
  }
})


