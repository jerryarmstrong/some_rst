src/cli/mplex.ts
================

Last edited: 2022-10-10 15:06:28

Contents:

.. code-block:: ts

    import yargs from 'yargs/yargs'
import { hideBin } from 'yargs/helpers'
import { CandyMachineCreateArgs, devClusters } from '@/types'
import { strict as assert } from 'assert'
import { cmdAirdrop } from '@/commands/airdrop'
import { closeConnection } from '@/utils/connection'
import { logError } from '@/utils'
import { BigNumber } from '@metaplex-foundation/js'
import { checked, mplex } from './flags'
import { cmdCandyMachineCreate } from '@/commands/candy-machine'
import { resolveIdentity } from '@/utils/identity'
import { tweakConfirmOptions } from '@/utils/amman'

const commands = yargs(hideBin(process.argv))
  // -----------------
  // Airdrop
  // -----------------
  .command(
    'airdrop',
    `Drops the amount of sols to the provided address (only works for ${devClusters} clusters)`,
    (args) => {
      mplex(args)
        .cluster()
        .commitment()
        .positional('pubkey', {
          describe: 'The pubkey to which we want to drop the SOL.',
          type: 'string',
          demandOption: true,
        })
        .positional('amount', {
          describe: 'Amount of SOL to drop.',
          type: 'string',
          default: 1,
        })
    }
  )
  // -----------------
  // CM (Candy Machine)
  // -----------------
  .command('cm', 'Creates and interacts with candy machines', (args) => {
    args
      .command('create', 'Create a new Candy Machine', (args) => {
        mplex(args).cluster().commitment().keypair().items().points()
      })
      .command('update', 'Update an existing Candy Machine', (_args) => {})
      .command(
        'insert',
        'Insert items into an existing Candy Machine',
        (_args) => {}
      )
      .command('delete', 'Delete an existing Candy Machine', (_args) => {})
      .command('mint', 'Mint from an existing Candy Machine', (_args) => {})
      .command(
        'find',
        'Finds an existing Candy Machine by its addres (includes Candy Guard if any)',
        (_args) => {}
      )
      // -----------------
      // CM Candy Guards
      // -----------------
      .command(
        'cg',
        'Creates and interacts with candy machine guards',
        (args) => {
          args
            .command('create', 'Creates a new Candy Guard', (_args) => {})
            .command('update', 'Updates an existing Candy Guard', (_args) => {})
            .command('delete', 'Deletes an existing Candy Guard', (_args) => {})
            .command(
              'find',
              'Finds an existing Candy Guard by address or authority',
              (_args) => {}
            )
            .command('wrap', 'Wraps an existing Candy Guard', (_args) => {})
            .command('unwrap', 'Unwraps an existing Candy Guard', (_args) => {})
        }
      )
  })

async function main() {
  const args = await commands.parse()
  const { _: cs } = args
  if (cs.length === 0) {
    commands.showHelp()
    return
  }
  const [cmd, sub1, sub2] = cs
  switch (cmd) {
    // -----------------
    // airdrop
    // -----------------
    case 'airdrop': {
      try {
        const { commitment, cluster } = checked(args)

        const destination = sub1
        const maybeAmount = sub2
        const amount =
          maybeAmount == null
            ? 1
            : typeof maybeAmount === 'string'
            ? parseInt(maybeAmount)
            : maybeAmount

        assert(
          typeof destination === 'string',
          'Destination public key string is required'
        )

        const { connection } = await cmdAirdrop(
          cluster,
          commitment,
          destination,
          amount
        )

        await closeConnection(connection, true)
      } catch (err) {
        logError(err)
        commands.showHelp()
      }
      break
    }
    // -----------------
    // CandyMachine Create
    // -----------------
    case 'cm': {
      switch (sub1) {
        case 'cg': {
          logError('CandyGuard not yet handled')
          break
        }
        case 'create': {
          const { commitment, cluster, keypair } = checked(args)
          const itemsAvailable = args.items as BigNumber
          const sellerFeeBasisPoints = args.points as number
          const identity = resolveIdentity(keypair)
          const createArgs = tweakConfirmOptions<CandyMachineCreateArgs>({
            itemsAvailable,
            sellerFeeBasisPoints,
          })
          await cmdCandyMachineCreate(cluster, commitment, identity, createArgs)
          break
        }
        default: {
          logError('CandyMachine subcommand %s not yet handled', sub1)
        }
      }
    }
  }
}

main()
  .then(() => process.nextTick(() => process.exit(0)))
  .catch((err: any) => {
    console.error(err)
    process.exit(1)
  })


