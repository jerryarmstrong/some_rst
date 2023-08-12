packages/sdk/test/setup/txs-init.ts
===================================

Last edited: 2023-06-14 20:00:41

Contents:

.. code-block:: ts

    import {
  ConfirmedTransactionAssertablePromise,
  GenLabeledKeypair,
  LoadOrGenKeypair,
  LOCALHOST,
  PayerTransactionHandler,
} from '@metaplex-foundation/amman-client';
import {
  createCreateMetadataAccountV3Instruction,
  CreateMasterEditionInstructionAccounts,
  CreateMetadataAccountV3InstructionArgs,
  CreateMetadataAccountV3InstructionAccounts,
  createCreateMasterEditionInstruction,
  CreateMasterEditionInstructionArgs,
} from '@metaplex-foundation/mpl-token-metadata';
import {
  createInitializeInstruction,
  InitializeInstructionArgs,
  InitializeArgs,
  InitializeInstructionAccounts,
  CloseInstructionAccounts,
  createCloseInstruction,
  UpdateArgs,
  UpdateInstructionAccounts,
  createUpdateInstruction,
  UpdateInstructionArgs,
} from '../../src/generated';
import {
  ASSOCIATED_TOKEN_PROGRAM_ID,
  TOKEN_PROGRAM_ID,
  MintLayout,
  createInitializeMintInstruction,
  getAssociatedTokenAddress,
  createAssociatedTokenAccountInstruction,
  createMintToInstruction,
} from '@solana/spl-token';
import { Connection, Keypair, PublicKey, SystemProgram, Transaction } from '@solana/web3.js';
import { amman } from '.';
import { findEditionAddress, findMetadataAddress, findMigrationState } from '../utils/pdas';

export class InitTransactions {
  readonly getKeypair: LoadOrGenKeypair | GenLabeledKeypair;

  constructor(readonly resuseKeypairs = false) {
    this.getKeypair = resuseKeypairs ? amman.loadOrGenKeypair : amman.genLabeledKeypair;
  }

  async payer() {
    const [payer, payerPair] = await this.getKeypair('Payer');

    const connection = new Connection(LOCALHOST, 'confirmed');
    await amman.airdrop(connection, payer, 2);

    const transactionHandler = amman.payerTransactionHandler(connection, payerPair);

    return {
      fstTxHandler: transactionHandler,
      connection,
      payer,
      payerPair,
    };
  }

  async initialize(
    handler: PayerTransactionHandler,
    payer: Keypair,
    authority: Keypair,
    collectionMint: PublicKey,
    args: InitializeArgs,
  ): Promise<{
    tx: ConfirmedTransactionAssertablePromise;
    migrationState: PublicKey;
  }> {
    amman.addr.addLabel('Authority', authority.publicKey);
    amman.addr.addLabel('Collection Mint', collectionMint);

    const collectionMetadata = findMetadataAddress(collectionMint);
    const migrationState = findMigrationState(collectionMint);

    const accounts: InitializeInstructionAccounts = {
      payer: payer.publicKey,
      authority: authority.publicKey,
      collectionMetadata,
      collectionMint,
      migrationState,
      systemProgram: SystemProgram.programId,
    };

    const ixArgs: InitializeInstructionArgs = {
      initializeArgs: args,
    };
    const initializeIx = createInitializeInstruction(accounts, ixArgs);

    const tx = new Transaction().add(initializeIx);
    const signers = [payer, authority];

    return {
      tx: handler.sendAndConfirmTransaction(tx, signers, 'tx: Initialize'),
      migrationState,
    };
  }

  async close(
    handler: PayerTransactionHandler,
    authority: Keypair,
    migrationState: PublicKey,
  ): Promise<{
    tx: ConfirmedTransactionAssertablePromise;
    migrationState: PublicKey;
  }> {
    amman.addr.addLabel('Authority', authority.publicKey);
    amman.addr.addLabel('Migration State', migrationState);

    const accounts: CloseInstructionAccounts = {
      authority: authority.publicKey,
      migrationState,
      systemProgram: SystemProgram.programId,
    };

    const closeIx = createCloseInstruction(accounts);

    const tx = new Transaction().add(closeIx);
    const signers = [authority];

    return {
      tx: handler.sendAndConfirmTransaction(tx, signers, 'tx: Close'),
      migrationState,
    };
  }

  async update(
    handler: PayerTransactionHandler,
    authority: Keypair,
    migrationState: PublicKey,
    args: UpdateArgs,
  ): Promise<{
    tx: ConfirmedTransactionAssertablePromise;
    migrationState: PublicKey;
  }> {
    amman.addr.addLabel('Authority', authority.publicKey);
    amman.addr.addLabel('Migration State', migrationState);

    const accounts: UpdateInstructionAccounts = {
      authority: authority.publicKey,
      migrationState,
    };

    const ixArgs: UpdateInstructionArgs = {
      updateArgs: args,
    };

    const updateIx = createUpdateInstruction(accounts, ixArgs);

    const tx = new Transaction().add(updateIx);
    const signers = [authority];

    return {
      tx: handler.sendAndConfirmTransaction(tx, signers, 'tx: Update'),
      migrationState,
    };
  }

  async mintNft(
    handler: PayerTransactionHandler,
    connection: Connection,
    payer: Keypair,
    authority: Keypair,
  ): Promise<{
    tx: ConfirmedTransactionAssertablePromise;
    metadata: PublicKey;
    masterEdition: PublicKey;
    mint: PublicKey;
  }> {
    amman.addr.addLabel('Authority', authority.publicKey);

    const mint = new Keypair();

    // Allocate memory for the account
    const mintRent = await connection.getMinimumBalanceForRentExemption(MintLayout.span);

    // Create mint account
    const createMintAccountIx = SystemProgram.createAccount({
      fromPubkey: payer.publicKey,
      newAccountPubkey: mint.publicKey,
      lamports: mintRent,
      space: MintLayout.span,
      programId: TOKEN_PROGRAM_ID,
    });

    // Initalize mint ix
    // Creator keypair is mint and freeze authority
    const initMintIx = createInitializeMintInstruction(
      mint.publicKey,
      0,
      authority.publicKey,
      authority.publicKey,
      TOKEN_PROGRAM_ID,
    );

    const ata = await getAssociatedTokenAddress(
      mint.publicKey,
      authority.publicKey,
      false,
      TOKEN_PROGRAM_ID,
      ASSOCIATED_TOKEN_PROGRAM_ID,
    );

    // Create associated account for user
    const assoc = createAssociatedTokenAccountInstruction(
      payer.publicKey,
      ata,
      authority.publicKey,
      mint.publicKey,
      TOKEN_PROGRAM_ID,
      ASSOCIATED_TOKEN_PROGRAM_ID,
    );

    // Create mintTo ix; mint to user's associated account
    const mintToIx = createMintToInstruction(
      mint.publicKey,
      ata,
      authority.publicKey, // Mint authority
      1,
      [], // No multi-sign signers
      TOKEN_PROGRAM_ID,
    );

    // Derive PDAs
    const metadata = findMetadataAddress(mint.publicKey);
    const masterEdition = findEditionAddress(mint.publicKey);

    const accounts: CreateMetadataAccountV3InstructionAccounts = {
      metadata,
      mint: mint.publicKey,
      mintAuthority: authority.publicKey,
      payer: payer.publicKey,
      updateAuthority: authority.publicKey,
      systemProgram: SystemProgram.programId,
    };

    const args: CreateMetadataAccountV3InstructionArgs = {
      createMetadataAccountArgsV3: {
        data: {
          name: 'Test',
          symbol: 'TEST',
          uri: 'https://test.com',
          sellerFeeBasisPoints: 0,
          creators: [
            {
              address: authority.publicKey,
              verified: true,
              share: 100,
            },
          ],
          collection: null,
          uses: null,
        },
        isMutable: true,
        collectionDetails: null,
      },
    };

    const createMetadataIx = createCreateMetadataAccountV3Instruction(accounts, args);

    const editionAccounts: CreateMasterEditionInstructionAccounts = {
      metadata,
      edition: masterEdition,
      mint: mint.publicKey,
      mintAuthority: authority.publicKey,
      payer: payer.publicKey,
      updateAuthority: authority.publicKey,
      systemProgram: SystemProgram.programId,
    };

    const editionArgs: CreateMasterEditionInstructionArgs = {
      createMasterEditionArgs: {
        maxSupply: 1,
      },
    };

    const createEditionIx = createCreateMasterEditionInstruction(editionAccounts, editionArgs);

    const tx = new Transaction().add(
      createMintAccountIx,
      initMintIx,
      assoc,
      mintToIx,
      createMetadataIx,
      createEditionIx,
    );
    const signers = [payer, authority, mint];

    return {
      tx: handler.sendAndConfirmTransaction(tx, signers, 'tx: Initialize'),
      metadata,
      masterEdition,
      mint: mint.publicKey,
    };
  }
}


