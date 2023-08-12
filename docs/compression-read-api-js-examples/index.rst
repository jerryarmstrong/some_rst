index.ts
========

Last edited: 2023-01-11 16:09:36

Contents:

.. code-block:: ts

    import {
  bufferToArray,
  execute,
  getVoucherPDA,
  getBubblegumAuthorityPDA,
  getMasterEdition,
  getMetadata,
} from "./helpers";
import {
  PROGRAM_ID as TOKEN_METADATA_PROGRAM_ID,
  TokenStandard,
  createCreateMetadataAccountV3Instruction,
  createCreateMasterEditionV3Instruction,
  createSetCollectionSizeInstruction,
} from "@metaplex-foundation/mpl-token-metadata";
import {
  ASSOCIATED_TOKEN_PROGRAM_ID,
  Token,
  TOKEN_PROGRAM_ID,
} from "@solana/spl-token";
import {
  Keypair,
  // LAMPORTS_PER_SOL,
  PublicKey,
  sendAndConfirmTransaction,
  Signer,
  SystemProgram,
  SYSVAR_RENT_PUBKEY,
  Transaction,
  LAMPORTS_PER_SOL,
  AccountMeta,
} from "@solana/web3.js";
import { WrappedConnection } from "./wrappedConnection";
import { bs58 } from "@project-serum/anchor/dist/cjs/utils/bytes";
import { BN } from "@project-serum/anchor";
import {
  TokenProgramVersion,
  createCreateTreeInstruction,
  PROGRAM_ID as BUBBLEGUM_PROGRAM_ID,
  createTransferInstruction,
  createDecompressV1Instruction,
  createRedeemInstruction,
  MetadataArgs,
  Creator,
  createMintToCollectionV1Instruction,
} from "@metaplex-foundation/mpl-bubblegum";
import {
  SPL_ACCOUNT_COMPRESSION_PROGRAM_ID,
  getConcurrentMerkleTreeAccountSize,
  SPL_NOOP_PROGRAM_ID,
  ConcurrentMerkleTreeAccount,
} from "@solana/spl-account-compression";

Error.stackTraceLimit = Infinity;
const makeCompressedNFT = (
  name: string,
  symbol: string,
  creators: Creator[] = []
) => {
  return {
    name: "Degen Ape #1338",
    symbol: "DAPE",
    uri: "https://arweave.net/gfO_TkYttQls70pTmhrdMDz9pfMUXX8hZkaoIivQjGs",
    creators: [],
    editionNonce: 253,
    tokenProgramVersion: TokenProgramVersion.Original,
    tokenStandard: TokenStandard.NonFungible,
    uses: null,
    collection: null,
    primarySaleHappened: false,
    sellerFeeBasisPoints: 0,
    isMutable: false,
  };
};

const sleep = async (ms: any) => {
  return new Promise((resolve) => setTimeout(resolve, ms));
};

const mapProof = (assetProof: { proof: string[] }): AccountMeta[] => {
  if (!assetProof.proof || assetProof.proof.length === 0) {
    throw new Error("Proof is empty");
  }
  return assetProof.proof.map((node) => ({
    pubkey: new PublicKey(node),
    isSigner: false,
    isWritable: false,
  }));
};

/*


CREATE A NEW TREE and Mint one compressed NFT


*/

const setupTreeWithCompressedNFT = async (
  connectionWrapper: WrappedConnection,
  payerKeypair: Keypair,
  compressedNFT: MetadataArgs,
  maxDepth: number = 14,
  maxBufferSize: number = 64
) => {
  const payer = payerKeypair.publicKey;
  const merkleTreeKeypair = Keypair.generate();
  const merkleTree = merkleTreeKeypair.publicKey;
  const space = getConcurrentMerkleTreeAccountSize(maxDepth, maxBufferSize, 5);
  const collectionMint = await Token.createMint(
    connectionWrapper,
    payerKeypair,
    payer,
    payer,
    0,
    TOKEN_PROGRAM_ID
  );
  const collectionTokenAccount = await collectionMint.createAccount(payer);
  await collectionMint.mintTo(collectionTokenAccount, payerKeypair, [], 1);
  const [colectionMetadataAccount, _b] = await PublicKey.findProgramAddress(
    [
      Buffer.from("metadata", "utf8"),
      TOKEN_METADATA_PROGRAM_ID.toBuffer(),
      collectionMint.publicKey.toBuffer(),
    ],
    TOKEN_METADATA_PROGRAM_ID
  );
  const collectionMeatadataIX = createCreateMetadataAccountV3Instruction(
    {
      metadata: colectionMetadataAccount,
      mint: collectionMint.publicKey,
      mintAuthority: payer,
      payer,
      updateAuthority: payer,
    },
    {
      createMetadataAccountArgsV3: {
        data: {
          name: "oh",
          symbol: "oh",
          uri: "oh",
          sellerFeeBasisPoints: 100,
          creators: null,
          collection: null,
          uses: null,
        },
        isMutable: false,
        collectionDetails: null,
      },
    }
  );
  const [collectionMasterEditionAccount, _b2] =
    await PublicKey.findProgramAddress(
      [
        Buffer.from("metadata", "utf8"),
        TOKEN_METADATA_PROGRAM_ID.toBuffer(),
        collectionMint.publicKey.toBuffer(),
        Buffer.from("edition", "utf8"),
      ],
      TOKEN_METADATA_PROGRAM_ID
    );
  const collectionMasterEditionIX = createCreateMasterEditionV3Instruction(
    {
      edition: collectionMasterEditionAccount,
      mint: collectionMint.publicKey,
      updateAuthority: payer,
      mintAuthority: payer,
      payer: payer,
      metadata: colectionMetadataAccount,
    },
    {
      createMasterEditionArgs: {
        maxSupply: 0,
      },
    }
  );

  const sizeCollectionIX = createSetCollectionSizeInstruction(
    {
      collectionMetadata: colectionMetadataAccount,
      collectionAuthority: payer,
      collectionMint: collectionMint.publicKey,
    },
    {
      setCollectionSizeArgs: { size: 0 },
    }
  );

  let tx_collection = new Transaction()
    .add(collectionMeatadataIX)
    .add(collectionMasterEditionIX)
    .add(sizeCollectionIX);
  tx_collection.feePayer = payer;
  await sendAndConfirmTransaction(
    connectionWrapper,
    tx_collection,
    [payerKeypair],
    {
      commitment: "confirmed",
      skipPreflight: true,
    }
  );

  const allocTreeIx = SystemProgram.createAccount({
    fromPubkey: payer,
    newAccountPubkey: merkleTree,
    lamports: await connectionWrapper.getMinimumBalanceForRentExemption(space),
    space: space,
    programId: SPL_ACCOUNT_COMPRESSION_PROGRAM_ID,
  });
  const [treeAuthority, _bump] = await PublicKey.findProgramAddress(
    [merkleTree.toBuffer()],
    BUBBLEGUM_PROGRAM_ID
  );
  const createTreeIx = createCreateTreeInstruction(
    {
      merkleTree,
      treeAuthority,
      treeCreator: payer,
      payer,
      logWrapper: SPL_NOOP_PROGRAM_ID,
      compressionProgram: SPL_ACCOUNT_COMPRESSION_PROGRAM_ID,
    },
    {
      maxBufferSize,
      maxDepth,
      public: false,
    },
    BUBBLEGUM_PROGRAM_ID
  );
  const [bgumSigner, __] = await PublicKey.findProgramAddress(
    [Buffer.from("collection_cpi", "utf8")],
    BUBBLEGUM_PROGRAM_ID
  );
  const mintIx = createMintToCollectionV1Instruction(
    {
      merkleTree,
      treeAuthority,
      treeDelegate: payer,
      payer,
      leafDelegate: payer,
      leafOwner: payer,
      compressionProgram: SPL_ACCOUNT_COMPRESSION_PROGRAM_ID,
      logWrapper: SPL_NOOP_PROGRAM_ID,
      collectionAuthority: payer,
      collectionAuthorityRecordPda: BUBBLEGUM_PROGRAM_ID,
      collectionMint: collectionMint.publicKey,
      collectionMetadata: colectionMetadataAccount,
      editionAccount: collectionMasterEditionAccount,
      bubblegumSigner: bgumSigner,
      tokenMetadataProgram: TOKEN_METADATA_PROGRAM_ID,
    },
    {
      metadataArgs: Object.assign(compressedNFT, {
        collection: { key: collectionMint.publicKey, verified: false },
      }),
    }
  );
  let tx = new Transaction().add(allocTreeIx).add(createTreeIx);
  tx.feePayer = payer;
  await sendAndConfirmTransaction(
    connectionWrapper,
    tx,
    [merkleTreeKeypair, payerKeypair],
    {
      commitment: "confirmed",
      skipPreflight: true,
    }
  );
  tx = new Transaction().add(mintIx);
  tx.feePayer = payer;
  await sendAndConfirmTransaction(connectionWrapper, tx, [payerKeypair], {
    commitment: "confirmed",
    skipPreflight: true,
  });
  return {
    merkleTree,
  };
};
//@ts-ignore
const transferAsset = async (
  connectionWrapper: WrappedConnection,
  newOwner: Keypair,
  canopyHeight: number | undefined,
  assetId: string
) => {
  console.log("transfer");
  let assetProof = await connectionWrapper.getAssetProof(assetId);
  let proofPath = mapProof(assetProof);
  const rpcAsset = await connectionWrapper.getAsset(assetId);

  const leafNonce = rpcAsset.compression.leaf_id;
  const treeAuthority = await getBubblegumAuthorityPDA(
    new PublicKey(assetProof.tree_id)
  );
  const leafDelegate = rpcAsset.ownership.delegate
    ? new PublicKey(rpcAsset.ownership.delegate)
    : new PublicKey(rpcAsset.ownership.owner);
  let transferIx = createTransferInstruction(
    {
      treeAuthority,
      leafOwner: new PublicKey(rpcAsset.ownership.owner),
      leafDelegate: leafDelegate,
      newLeafOwner: newOwner.publicKey,
      merkleTree: new PublicKey(assetProof.tree_id),
      logWrapper: SPL_NOOP_PROGRAM_ID,
      compressionProgram: SPL_ACCOUNT_COMPRESSION_PROGRAM_ID,
      anchorRemainingAccounts: proofPath.slice(
        0,
        proofPath.length - (!!canopyHeight ? canopyHeight : 0)
      ),
    },
    {
      root: bufferToArray(bs58.decode(assetProof.root)),
      dataHash: bufferToArray(
        bs58.decode(rpcAsset.compression.data_hash.trim())
      ),
      creatorHash: bufferToArray(
        bs58.decode(rpcAsset.compression.creator_hash.trim())
      ),
      nonce: leafNonce,
      index: leafNonce,
    }
  );
  await execute(
    connectionWrapper.provider,
    [transferIx],
    [connectionWrapper.payer],
    true
  );
};
const redeemAsset = async (
  connectionWrapper: WrappedConnection,
  canopyHeight: number | undefined,
  payer?: Keypair,
  assetId?: string
) => {
  console.log("redeem");
  let assetProof = await connectionWrapper.getAssetProof(assetId);
  const rpcAsset = await connectionWrapper.getAsset(assetId);
  const voucher = await getVoucherPDA(new PublicKey(assetProof.tree_id), 0);
  const leafNonce = rpcAsset.compression.leaf_id;
  const treeAuthority = await getBubblegumAuthorityPDA(
    new PublicKey(assetProof.tree_id)
  );
  const leafDelegate = rpcAsset.ownership.delegate
    ? new PublicKey(rpcAsset.ownership.delegate)
    : new PublicKey(rpcAsset.ownership.owner);
  const redeemIx = createRedeemInstruction(
    {
      treeAuthority,
      leafOwner: new PublicKey(rpcAsset.ownership.owner),
      leafDelegate,
      merkleTree: new PublicKey(assetProof.tree_id),
      voucher,
      logWrapper: SPL_NOOP_PROGRAM_ID,
      compressionProgram: SPL_ACCOUNT_COMPRESSION_PROGRAM_ID,
    },
    {
      root: bufferToArray(bs58.decode(assetProof.root)),
      dataHash: bufferToArray(
        bs58.decode(rpcAsset.compression.data_hash.trim())
      ),
      creatorHash: bufferToArray(
        bs58.decode(rpcAsset.compression.creator_hash.trim())
      ),
      nonce: leafNonce,
      index: leafNonce,
    }
  );
  const _payer = payer ? payer : connectionWrapper.provider.wallet;
  await execute(
    connectionWrapper.provider,
    [redeemIx],
    [_payer as Signer],
    true
  );
};

async function decompressAsset(
  connectionWrapper: WrappedConnection,
  canopyHeight: number | undefined,
  payer?: Keypair,
  assetId?: string
) {
  console.log("decompress ", assetId);
  let assetProof = await connectionWrapper.getAssetProof(assetId);
  let proofPath = mapProof(assetProof);
  const rpcAsset = await connectionWrapper.getAsset(assetId);
  const voucher = await getVoucherPDA(new PublicKey(assetProof.tree_id), 0);
  const leafNonce = rpcAsset.compression.leaf_id;

  await redeemAsset(connectionWrapper, canopyHeight, payer, assetId);

  let [assetPDA] = await PublicKey.findProgramAddress(
    [
      Buffer.from("asset"),
      new PublicKey(assetProof.tree_id).toBuffer(),
      leafNonce.toBuffer("le", 8),
    ],
    BUBBLEGUM_PROGRAM_ID
  );
  const [mintAuthority] = await PublicKey.findProgramAddress(
    [assetPDA.toBuffer()],
    BUBBLEGUM_PROGRAM_ID
  );

  sleep(20000);
  const assetAgain = await connectionWrapper.getAsset(rpcAsset.id);

  const metadata: MetadataArgs = {
    name: rpcAsset.content.metadata.name,
    symbol: rpcAsset.content.metadata.symbol,
    uri: rpcAsset.content.json_uri,
    sellerFeeBasisPoints: rpcAsset.royalty.basis_points,
    primarySaleHappened: rpcAsset.royalty.primary_sale_happened,
    isMutable: rpcAsset.mutable,
    editionNonce: rpcAsset.supply.edition_nonce,
    tokenStandard: TokenStandard.NonFungible,
    collection: rpcAsset.grouping,
    uses: rpcAsset.uses,
    tokenProgramVersion: TokenProgramVersion.Original,
    creators: rpcAsset.creators,
  };

  const decompressIx = createDecompressV1Instruction(
    {
      voucher: voucher,
      leafOwner: new PublicKey(assetAgain.ownership.owner),
      tokenAccount: await Token.getAssociatedTokenAddress(
        ASSOCIATED_TOKEN_PROGRAM_ID,
        TOKEN_PROGRAM_ID,
        new PublicKey(assetAgain.id),
        new PublicKey(assetAgain.ownership.owner)
      ),
      mint: new PublicKey(assetAgain.id),
      mintAuthority: mintAuthority,
      metadata: await getMetadata(new PublicKey(assetAgain.id)),
      masterEdition: await getMasterEdition(new PublicKey(assetAgain.id)),
      sysvarRent: SYSVAR_RENT_PUBKEY,
      tokenMetadataProgram: TOKEN_METADATA_PROGRAM_ID,
      associatedTokenProgram: ASSOCIATED_TOKEN_PROGRAM_ID,
      logWrapper: SPL_NOOP_PROGRAM_ID,
      anchorRemainingAccounts: proofPath.slice(
        0,
        proofPath.length - (!!canopyHeight ? canopyHeight : 0)
      ),
    },
    {
      // this can be grabbed onChain by using the metadataArgsBeet.deserialize
      // currently there is an error inside beet program while using it
      metadata,
    }
  );
  const _payer = payer ? payer : connectionWrapper.provider.wallet;
  await execute(
    connectionWrapper.provider,
    [decompressIx],
    [_payer as Signer],
    true
  );
}

const wholeFlow = async () => {
  const rpcUrl = "https://rpc-devnet.aws.metaplex.com/";
  const connectionString =
    "https://liquid.devnet.rpcpool.com/5ebea512d12be102f53d319dafc8";
  // set up connection object
  // provides all connection functions and rpc functions
  const connectionWrapper = new WrappedConnection(
    Keypair.fromSeed(new TextEncoder().encode("hello world".padEnd(32, "\0"))),
    connectionString,
    rpcUrl
  );

  // await connectionWrapper.requestAirdrop(
  //   connectionWrapper.payer.publicKey,
  //   LAMPORTS_PER_SOL
  // );
  console.log("payer", connectionWrapper.provider.wallet.publicKey.toBase58());
  // returns filled out metadata args struct, doesn't actually do anything mint wise
  let originalCompressedNFT = makeCompressedNFT("test", "TST", []);
  // creates  and executes the merkle tree ix
  // and the mint ix is executed here as well
  let result = await setupTreeWithCompressedNFT(
    connectionWrapper,
    connectionWrapper.payer,
    originalCompressedNFT,
    14,
    64
  );
  const merkleTree = result.merkleTree;
  let mkAccount = await ConcurrentMerkleTreeAccount.fromAccountAddress(
    connectionWrapper,
    merkleTree
  );
  let canopyHeight = mkAccount.getCanopyDepth();
  const leafIndex = new BN.BN(0);
  // grabbing the asset id so that it can be passed to transfer
  const [assetId] = await PublicKey.findProgramAddress(
    [
      Buffer.from("asset", "utf8"),
      merkleTree.toBuffer(),
      Uint8Array.from(leafIndex.toArray("le", 8)),
    ],
    BUBBLEGUM_PROGRAM_ID
  );

  await sleep(15000);
  const assetString = assetId.toBase58();
  const newOwner = Keypair.generate();
  console.log("new owner", newOwner.publicKey.toBase58());
  sleep(120000);
  console.log(assetString)
  await execute(
    connectionWrapper.provider,
    [
      SystemProgram.transfer({
        fromPubkey: connectionWrapper.provider.publicKey,
        toPubkey: newOwner.publicKey,
        lamports: LAMPORTS_PER_SOL,
      }),
    ],
    [connectionWrapper.payer],
    true
  );

  //transferring the compressed asset to a new owner
  await transferAsset(connectionWrapper, newOwner, canopyHeight, assetString);
  // asset has to be redeemed before it can be decompressed
  // redeem is included above as a separate function because it can be called
  // without decompressing nftbut it is also called
  // inside of decompress so we don't need to call that separately here
  sleep(15000);

  await decompressAsset(connectionWrapper, canopyHeight, newOwner, assetString);
};

wholeFlow();


