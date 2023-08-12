src/cli/flags.ts
================

Last edited: 2022-10-10 15:06:28

Contents:

.. code-block:: ts

    import { Argv } from 'yargs'
import {
  assertCommitment,
  assertDevCluster,
  commitments,
  devClusters,
} from '@/types'
import { strict as assert } from 'assert'
import { keypairFromFileSync, resolvePath } from '@/utils/fs'
import { MplexAmman } from '@/utils/amman'

class MplexArgs {
  constructor(private readonly _args: Argv) {}

  cluster(
    describe = 'The cluster on which to perform the transaction. Defaults to MPLEX_CLUSTER or "devnet".'
  ) {
    this._args.option('cluster', {
      alias: 'c',
      describe,
      type: 'string',
      choices: devClusters,
      default: process.env.MPLEX_CLUSTER ?? 'devnet',
    })
    return this
  }

  commitment(describe = 'The commitment of the transaction') {
    this._args.option('commitment', {
      alias: 'm',
      describe,
      type: 'string',
      choices: commitments,
      default: 'singleGossip',
    })
    return this
  }

  keypair(
    describe = 'The path to the keypair JSON file to retreive the keypair to use for the transacion. If not provided transactions will be signed via you browser wallet'
  ) {
    this._args.option('keypair', {
      alias: 'k',
      describe,
      type: 'string',
    })
    return this
  }

  // -----------------
  // Candy Machine specific
  // -----------------
  items(describe = 'The amount fo Candy Machine items available') {
    this._args.option('items', {
      alias: 'i',
      describe,
      type: 'number',
      demandOption: true,
    })
    return this
  }

  points(describe = 'The Candy Machine seller fee basis points') {
    this._args.option('points', {
      alias: 'p',
      describe,
      type: 'number',
      demandOption: true,
    })
    return this
  }

  get positional() {
    return this._args.positional.bind(this._args)
  }
  get option() {
    return this._args.option.bind(this._args)
  }
}

type MplexArgsUnchecked =
  | Record<'cluster' | 'commitment' | 'keypair', any>
  | Record<string, any>
class MplexArgsChecked {
  constructor(private readonly _args: MplexArgsUnchecked) {}

  get cluster() {
    const cluster = this._args.cluster

    assert(typeof cluster === 'string', 'Cluster needs to be a string')
    assertDevCluster(cluster)

    MplexAmman.init(cluster)

    return cluster
  }

  get commitment() {
    const commitment = this._args.commitment
    assert(typeof commitment === 'string', 'Commitment needs to be a string')
    assertCommitment(commitment)
    return commitment
  }

  get keypair() {
    const keypair = this._args.keypair
    if (keypair == null) return undefined

    const fullPath = resolvePath(keypair)
    return keypairFromFileSync(fullPath)
  }
}

export function mplex(args: Argv) {
  return new MplexArgs(args)
}

export function checked(args: MplexArgsUnchecked) {
  return new MplexArgsChecked(args)
}


