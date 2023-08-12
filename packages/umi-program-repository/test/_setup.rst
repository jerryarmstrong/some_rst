packages/umi-program-repository/test/_setup.ts
==============================================

Last edited: 2023-07-27 15:49:41

Contents:

.. code-block:: ts

    import {
  Cluster,
  PublicKeyInput,
  RpcInterface,
  createUmi as baseCreateUmi,
  defaultPublicKey,
  publicKey,
} from '@metaplex-foundation/umi';
import { defaultProgramRepository } from '../src';

export const createUmi = (cluster: Cluster = 'localnet') => {
  const umi = baseCreateUmi().use(defaultProgramRepository());
  umi.rpc = { getCluster: () => cluster } as RpcInterface;
  return umi;
};

export const createProgram = (
  name: string,
  publicKeyInput: PublicKeyInput = defaultPublicKey()
) => ({
  name,
  publicKey: publicKey(publicKeyInput),
  getErrorFromCode: () => null,
  getErrorFromName: () => null,
  isOnCluster: () => true,
});


