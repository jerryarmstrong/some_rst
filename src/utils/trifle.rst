src/utils/trifle.ts
===================

Last edited: 2023-03-12 23:06:11

Contents:

.. code-block:: ts

    import { Connection, PublicKey, SYSVAR_INSTRUCTIONS_PUBKEY, Transaction, TransactionInstruction, TransactionMessage, VersionedTransaction } from "@solana/web3.js";
import { PROGRAM_ADDRESS as TRIFLE_PROGRAM_ADDRESS, createCreateTrifleAccountInstruction, EscrowConstraintModel, Trifle, createTransferInInstruction, createTransferOutInstruction } from '@metaplex-foundation/mpl-trifle';
import { PROGRAM_ADDRESS as TOKEN_METADATA_PROGRAM_ADDRESS } from '@metaplex-foundation/mpl-token-metadata';
import { Metaplex, Nft, NftWithToken, Sft, SftWithToken } from "@metaplex-foundation/js";
import { WalletContextState } from "@solana/wallet-adapter-react";
import { getAssociatedTokenAddress, TOKEN_PROGRAM_ID, ASSOCIATED_TOKEN_PROGRAM_ID, getAssociatedTokenAddressSync } from "@solana/spl-token";

export const findTriflePda = (
    mint: PublicKey,
    authority: PublicKey,
) => {
    return PublicKey.findProgramAddressSync(
        [
            Buffer.from("trifle"),
            mint.toBuffer(),
            authority.toBuffer(),
        ],
        new PublicKey(TRIFLE_PROGRAM_ADDRESS),
    );
};

export const findEscrowPda = (
    mint: PublicKey,
    authority: 0 | 1,
    creator?: PublicKey,
) => {
    let seeds = [
        Buffer.from("metadata"),
        new PublicKey(TOKEN_METADATA_PROGRAM_ADDRESS).toBuffer(),
        mint.toBuffer(),
        Uint8Array.from([authority]),
    ];

    if (authority == 1) {
        if (creator) {
            seeds.push(creator.toBuffer());
        } else {
            throw new Error("Creator is required");
        }
    }

    seeds.push(Buffer.from("escrow"));
    return PublicKey.findProgramAddressSync(
        seeds,
        new PublicKey(TOKEN_METADATA_PROGRAM_ADDRESS),
    );
};

export const createTrifleAccount = async (connection: Connection, selectedNFT: Nft, wallet: WalletContextState) => {
    const escrowConstraintModelAddress = process.env.NEXT_PUBLIC_CONSTRAINT_MODEL_ADDRESS;
    if (!wallet.publicKey) {
        console.log("Wallet not connected");
        return;
    }

    if (!escrowConstraintModelAddress) {
        console.log("Please select an escrow constraint model");
        return;
    }

    let selectedNFTTokenAccountAddress = await getAssociatedTokenAddress(selectedNFT.address, wallet.publicKey);
    let selectedEscrowConstraintModelAddress = new PublicKey(escrowConstraintModelAddress);
    let trifleAuthority = new PublicKey(process.env.NEXT_PUBLIC_FUSION_AUTHORITY);
    console.log("trifleAuthority: ", trifleAuthority.toString());
    let [trifleAddress] = findTriflePda(selectedNFT.address, trifleAuthority);
    let [escrowAddress] = findEscrowPda(selectedNFT.address, 1, trifleAddress);

    const instructions: TransactionInstruction[] = [];

    instructions.push(createCreateTrifleAccountInstruction({
        escrow: escrowAddress,
        metadata: selectedNFT.metadataAddress,
        mint: selectedNFT.address,
        tokenAccount: selectedNFTTokenAccountAddress,
        edition: selectedNFT.edition.address,
        trifleAccount: trifleAddress,
        trifleAuthority: trifleAuthority,
        constraintModel: selectedEscrowConstraintModelAddress,
        payer: wallet.publicKey,
        tokenMetadataProgram: new PublicKey(TOKEN_METADATA_PROGRAM_ADDRESS),
        sysvarInstructions: SYSVAR_INSTRUCTIONS_PUBKEY,
    }));

    let blockhash = await connection
        .getLatestBlockhash()
        .then((res) => res.blockhash);

    // create v0 compatible message
    const messageV0 = new TransactionMessage({
        payerKey: wallet.publicKey,
        recentBlockhash: blockhash,
        instructions,
    }).compileToV0Message();

    const transaction = new VersionedTransaction(messageV0);

    // sign your transaction with the required `Signers`
    const userSignedTx = await wallet.signTransaction(transaction);

    const response = await fetch("/api/createTrifleAccountTx", {
        method: "POST",
        body: Buffer.from(userSignedTx.serialize()).toString("base64"),
    });
    const fullySignedTx = VersionedTransaction.deserialize(Uint8Array.from(Buffer.from((await response.json()).tx, "base64")));

    try {
        const txid = await connection.sendRawTransaction(fullySignedTx.serialize(), { skipPreflight: true });
        console.log("Trifle account created");
        console.log(txid);
    } catch (e) {
        console.log(e);
        console.log("Failed to create trifle account");
    }

}

export const getConstraintModel = async (connection: Connection, modelAddress: PublicKey) => {
    const accountInfo = await connection.getAccountInfo(modelAddress);
    if (accountInfo) {
        const account: EscrowConstraintModel =
            EscrowConstraintModel.fromAccountInfo(accountInfo)[0];
        return account;
    } else {
        console.log("Unable to fetch model account");
        return null;
    }
}

export const getTrifle = async (connection: Connection, mintAddress: PublicKey, trifleAuthority: PublicKey) => {
    const [triflePda] = findTriflePda(mintAddress, trifleAuthority);
    const trifleAccount = await connection.getAccountInfo(triflePda);
    if (trifleAccount) {
        const trifle = Trifle.fromAccountInfo(trifleAccount)[0];
        return trifle;
    } else {
        console.log("Unable to fetch Trifle account");
        return null;
    }
}

export const getTrifleNfts = async (connection: Connection, trifle: Trifle) => {
    const metaplex = new Metaplex(connection);
    const fusedTraits = Array.from(trifle.tokens.values()).map((tokenAmount) => tokenAmount.map((token) => token.mint)).flat();
    let nfts: (NftWithToken | SftWithToken)[] = [];
    for (const fusedTrait of fusedTraits) {
        const nft = await metaplex.nfts().findByMint({
            mintAddress: fusedTrait,
            tokenOwner: trifle.tokenEscrow
        });

        nfts.push(nft as (NftWithToken | SftWithToken));
    }

    return nfts;
}

export const fuseTraits = async (connection: Connection, wallet: WalletContextState, selectedParent: NftWithToken, selectedTraits: (NftWithToken | SftWithToken)[], trifleAuthority: PublicKey) => {
    console.log("Traits to Fuse: ", selectedTraits);
    // Set up accounts
    const [triflePda] = findTriflePda(selectedParent.mint.address, trifleAuthority);
    const trifleAccount = await connection.getAccountInfo(triflePda);
    const trifle = Trifle.fromAccountInfo(trifleAccount)[0];
    console.log(trifle);
    console.log(trifle.tokenEscrow.toString());
    const model = await getConstraintModel(connection, trifle.escrowConstraintModel);
    console.log(model);
    // const selectedTraitMints = selectedTraits.filter((trait) => trait != null).map((trait) => trait.mint.address);

    let instructions: TransactionInstruction[] = [];

    // Determine which traits to transfer out
    // const fusedTraits = Array.from(trifle.tokens.values()).map((tokenAmount) => tokenAmount.map((token) => token.mint)).flat();
    // for (const fusedTrait of fusedTraits) {
    //     console.log(fusedTrait.toString());
    //     if (!selectedTraitMints.includes(fusedTrait)) {
    //         // Transfer Out
    //         console.log("Transfer Out");
    //     }
    // }


    // Determine which traits to transfer in
    for (const selectedTrait of selectedTraits) {
        if (selectedTrait == null) {
            continue;
        }
        console.log(selectedTrait);
        // if (!fusedTraits.includes(selectedTrait.mint.address)) {
        // Transfer In
        console.log("Transfer In");
        const attributeDstToken = getAssociatedTokenAddressSync(selectedTrait.mint.address, trifle.tokenEscrow, true);

        instructions.push(createTransferInInstruction(
            {
                trifle: triflePda,
                trifleAuthority,
                payer: wallet.publicKey,
                constraintModel: trifle.escrowConstraintModel,
                escrow: trifle.tokenEscrow,
                escrowMint: selectedParent.mint.address,
                escrowToken: selectedParent.token.address,
                escrowEdition: selectedParent.edition.address,
                attributeMint: selectedTrait.mint.address,
                attributeSrcToken: selectedTrait.token.address,
                attributeDstToken,
                attributeMetadata: selectedTrait.metadataAddress,
                attributeEdition: (selectedTrait as Nft).edition.address,
                attributeCollectionMetadata: selectedTrait.collection.address,
                splToken: TOKEN_PROGRAM_ID,
                splAssociatedTokenAccount: ASSOCIATED_TOKEN_PROGRAM_ID,
                tokenMetadataProgram: new PublicKey(TOKEN_METADATA_PROGRAM_ADDRESS),
            },
            {
                transferInArgs: {
                    slot: selectedTrait.json.attributes[0].trait_type,
                    amount: 1,
                }
            }
        ));
        // }

        if (instructions.length >= 2) {
            await sendTx(connection, instructions, wallet);
            instructions = [];
        }
    }

    if (instructions.length > 0) {
        await sendTx(connection, instructions, wallet);
        instructions = [];
    }
}

const sendTx = async (connection: Connection, instructions: TransactionInstruction[], wallet: WalletContextState) => {
    let blockhash = await connection
        .getLatestBlockhash()
        .then((res) => res.blockhash);

    // create v0 compatible message
    const messageV0 = new TransactionMessage({
        payerKey: wallet.publicKey,
        recentBlockhash: blockhash,
        instructions,
    }).compileToV0Message();

    const transaction = new VersionedTransaction(messageV0);

    // sign your transaction with the required `Signers`
    const signedTx = await wallet.signTransaction(transaction);
    console.log(signedTx.serialize().length);

    try {
        const txid = await connection.sendRawTransaction(signedTx.serialize(), { skipPreflight: true });
        console.log("(De)Fused!");
        console.log(txid);
    } catch (e) {
        console.log(e);
        console.log("Failed to (de)fuse");
    }
}

export const defuseTraits = async (connection: Connection, wallet: WalletContextState, selectedParent: NftWithToken, selectedTraits: (NftWithToken | SftWithToken)[], trifleAuthority: PublicKey) => {
    console.log("Traits to Defuse: ", selectedTraits);
    // Set up accounts
    const [triflePda] = findTriflePda(selectedParent.mint.address, trifleAuthority);
    const trifleAccount = await connection.getAccountInfo(triflePda);
    const trifle = Trifle.fromAccountInfo(trifleAccount)[0];
    console.log(trifle);
    console.log(trifle.tokenEscrow.toString());
    const model = await getConstraintModel(connection, trifle.escrowConstraintModel);
    console.log(model);
    // const selectedTraitMints = selectedTraits.filter((trait) => trait != null).map((trait) => trait.mint.address);

    let instructions: TransactionInstruction[] = [];

    // Determine which traits to transfer out
    // const fusedTraits = Array.from(trifle.tokens.values()).map((tokenAmount) => tokenAmount.map((token) => token.mint)).flat();
    // for (const fusedTrait of fusedTraits) {
    //     console.log(fusedTrait.toString());
    //     if (!selectedTraitMints.includes(fusedTrait)) {
    //         // Transfer Out
    //         console.log("Transfer Out");
    //     }
    // }


    // Determine which traits to transfer in
    for (const selectedTrait of selectedTraits) {
        if (selectedTrait == null) {
            continue;
        }
        console.log(selectedTrait);
        // if (!fusedTraits.includes(selectedTrait.mint.address)) {
        // Transfer In
        console.log("Transfer Outs");
        const attributeDstTokenAccount = getAssociatedTokenAddressSync(selectedTrait.mint.address, wallet.publicKey, true);

        instructions.push(createTransferOutInstruction(
            {
                trifleAccount: triflePda,
                trifleAuthority,
                payer: wallet.publicKey,
                constraintModel: trifle.escrowConstraintModel,
                escrowAccount: trifle.tokenEscrow,
                escrowMint: selectedParent.mint.address,
                escrowTokenAccount: selectedParent.token.address,
                escrowEdition: selectedParent.edition.address,
                attributeMint: selectedTrait.mint.address,
                attributeSrcTokenAccount: selectedTrait.token.address,
                attributeDstTokenAccount,
                attributeMetadata: selectedTrait.metadataAddress,
                splToken: TOKEN_PROGRAM_ID,
                splAssociatedTokenAccount: ASSOCIATED_TOKEN_PROGRAM_ID,
                tokenMetadataProgram: new PublicKey(TOKEN_METADATA_PROGRAM_ADDRESS),
                escrowMetadata: selectedParent.metadataAddress,
                sysvarInstructions: SYSVAR_INSTRUCTIONS_PUBKEY
            },
            {
                transferOutArgs: {
                    slot: selectedTrait.json.attributes[0].trait_type,
                    amount: 1,
                }
            }
        ));
        // }

        if (instructions.length >= 2) {
            await sendTx(connection, instructions, wallet);
            instructions = [];
        }
    }

    if (instructions.length > 0) {
        await sendTx(connection, instructions, wallet);
        instructions = [];
    }
}

