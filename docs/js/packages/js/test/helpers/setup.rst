packages/js/test/helpers/setup.ts
=================================

Last edited: 2023-05-26 09:49:40

Contents:

.. code-block:: ts

    import { Commitment, Connection, Keypair } from '@solana/web3.js';
import { LOCALHOST } from '@metaplex-foundation/amman-client';
import { amman } from './amman';
import {
  Metaplex,
  guestIdentity,
  keypairIdentity,
  mockStorage,
  UploadMetadataInput,
  CreateNftInput,
  KeypairSigner,
  CreateSftInput,
  NftWithToken,
} from '@/index';

export type MetaplexTestOptions = {
  rpcEndpoint?: string;

  /** The level of commitment desired when querying the blockchain. */
  commitment?: Commitment;
  solsToAirdrop?: number;
};

export const metaplexGuest = (options: MetaplexTestOptions = {}) => {
  const connection = new Connection(options.rpcEndpoint ?? LOCALHOST, {
    commitment: options.commitment ?? 'confirmed',
  });

  return Metaplex.make(connection).use(guestIdentity()).use(mockStorage());
};

export const metaplex = async (options: MetaplexTestOptions = {}) => {
  const mx = metaplexGuest(options);
  const wallet = await createWallet(mx, options.solsToAirdrop);

  return mx.use(keypairIdentity(wallet as Keypair));
};

export const createWallet = async (
  mx: Metaplex,
  solsToAirdrop = 100
): Promise<KeypairSigner> => {
  const wallet = Keypair.generate();
  await amman.airdrop(mx.connection, wallet.publicKey, solsToAirdrop);

  return wallet;
};

export const createNft = async (
  mx: Metaplex,
  input: Partial<CreateNftInput & { json: UploadMetadataInput }> = {}
) => {
  const { uri } = await mx.nfts().uploadMetadata(input.json ?? {});
  const { nft } = await mx.nfts().create({
    uri,
    name: 'My NFT',
    sellerFeeBasisPoints: 200,
    ...input,
  });

  return nft as NftWithToken;
};

export const createCollectionNft = (
  mx: Metaplex,
  input: Partial<CreateNftInput & { json: UploadMetadataInput }> = {}
) => createNft(mx, { ...input, isCollection: true });

export const createSft = async (
  mx: Metaplex,
  input: Partial<CreateSftInput & { json: UploadMetadataInput }> = {}
) => {
  const { uri } = await mx.nfts().uploadMetadata(input.json ?? {});
  const { sft } = await mx.nfts().createSft({
    uri,
    name: 'My SFT',
    sellerFeeBasisPoints: 200,
    ...input,
  });

  return sft;
};


