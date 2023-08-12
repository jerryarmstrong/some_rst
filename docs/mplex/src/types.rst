src/types.ts
============

Last edited: 2022-10-10 15:06:28

Contents:

.. code-block:: ts

    import { Cluster, Commitment } from '@solana/web3.js'
import { strict as assert } from 'assert'
import {
  CreateCandyMachineInput,
  DefaultCandyGuardSettings,
  Cluster as SdkCluster,
} from '@metaplex-foundation/js'

// -----------------
// Clusters
// -----------------
export type ClusterWithLocal = Cluster | 'local'
export const clusters: Readonly<ClusterWithLocal[]> = [
  'devnet',
  'mainnet-beta',
  'testnet',
  'local',
] as const

export type DevCluster = 'devnet' | 'local'
export const devClusters: Readonly<DevCluster[]> = ['devnet', 'local'] as const

export function clusterWithLocalToSdkCluster(
  cluster: ClusterWithLocal
): SdkCluster {
  if (cluster === 'local') return 'localnet'
  return cluster
}

export function isDevCluster(value: string): value is DevCluster {
  return devClusters.includes(value as DevCluster)
}
export function assertDevCluster(value: string): asserts value is DevCluster {
  assert(isDevCluster(value), `Invalid dev cluster: ${value}`)
}

// -----------------
// Commitments
// -----------------
export const commitments: Readonly<Commitment[]> = [
  'processed',
  'confirmed',
  'finalized',
  'recent',
  'single',
  'singleGossip',
  'root',
  'max',
] as const

export function isCommitment(value: string): value is Commitment {
  return commitments.includes(value as Commitment)
}

export function assertCommitment(value: string): asserts value is Commitment {
  assert(isCommitment(value), `Invalid commitment: ${value}`)
}

// -----------------
// Generic Helpers
// -----------------
export type Optional<T, K extends keyof T> = Pick<Partial<T>, K> & Omit<T, K>

// -----------------
// CandyMachine
// -----------------
export type CandyMachineCreateArgs = Optional<
  CreateCandyMachineInput<DefaultCandyGuardSettings>,
  'collection'
>


