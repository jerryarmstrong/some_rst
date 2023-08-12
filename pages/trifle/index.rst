pages/trifle/index.tsx
======================

Last edited: 2023-02-28 18:04:35

Contents:

.. code-block:: tsx

    /* eslint-disable @next/next/no-img-element */
import { useState, useEffect, useMemo } from 'react';
import type { NextPage } from 'next'
import { Button, Container, Typography, Stack, ImageList, ImageListItem, Select, MenuItem } from '@mui/material'
import { useConnection, useWallet, WalletContextState } from '@solana/wallet-adapter-react';
import { useMetaplex } from '../../hooks/useMetaplex';
import { Metadata, Metaplex, Nft } from '@metaplex-foundation/js';
import { AccountInfo, Keypair, PublicKey, SYSVAR_INSTRUCTIONS_PUBKEY, Transaction } from '@solana/web3.js';
import { EscrowConstraintModel, createCreateTrifleAccountInstruction } from '@metaplex-foundation/mpl-trifle/dist/src/generated';
import { getAssociatedTokenAddress } from '@solana/spl-token';
import { TOKEN_PROGRAM_ID } from "@solana/spl-token"
import { findEscrowPda, findTriflePda } from '../../helpers/pdas';
import { loadEscrowConstraintModels } from '../../helpers/loadEscrowConstraintModels';
import { toast } from 'react-toastify';
import { loadTrifleNFTs } from '../../helpers/loadNFTs';
import { PROGRAM_ADDRESS as TOKEN_METADATA_PROGRAM_ID } from '@metaplex-foundation/mpl-token-metadata';

const METAPLEX_BUCKET = "Jf27xwhv6bH1aaPYtvJxvHvKRHoDe3DyQVqe4CJyxsP";

type EscrowConstraintModelWithPubkey = {
    pubkey: PublicKey,
    escrowConstraintModel: EscrowConstraintModel
}

const CreateTrifle: NextPage = () => {
    const wallet = useWallet();
    const { connection } = useConnection();
    const { metaplex } = useMetaplex();
    const [allNFTs, setAllNFTs] = useState<any[]>([]);
    // selected to become the base token
    const [selectedNFT, setSelectedNFT] = useState<any>(null);
    const [selectedEscrowConstraintModel, setSelectedEscrowConstraintModel] = useState<string>("");
    const [escrowConstraintModels, setEscrowConstraintModels] = useState<Record<string, EscrowConstraintModel>>({});

    useEffect(() => {
        if (!wallet.publicKey) {
            return;
        }
        if (!metaplex) {
            return;
        }

        loadTrifleNFTs(metaplex, wallet).then((nfts) => {
            setAllNFTs(nfts)
        })

        loadEscrowConstraintModels(wallet.publicKey, connection).then(models => {
            setEscrowConstraintModels(models)
        });
    }, [wallet.publicKey, metaplex, wallet, connection])


    const handleNFTClick = (nft: Metadata) => {
        console.log(nft);
        metaplex?.nfts().load({ metadata: nft }).then((loadedNFT: any) => {
            console.log({ loadedNFT });
            setSelectedNFT(loadedNFT);
        });
    }

    // TODO: type this function properly
    const handleCreateTrifleAccount = async (selectedNFT: any) => {
        if (!wallet.publicKey) {
            toast.error("Wallet not connected");
            return;
        }

        if (!selectedEscrowConstraintModel) {
            toast.error("Please select an escrow constraint model");
            return;
        }

        let selectedNFTTokenAccountAddress = await getAssociatedTokenAddress(selectedNFT.address, wallet.publicKey);
        let selectedEscrowConstraintModelAddress = new PublicKey(selectedEscrowConstraintModel);
        let [trifleAddress] = await findTriflePda(selectedNFT.address, wallet.publicKey);
        let [escrowAddress] = await findEscrowPda(selectedNFT.address, 1, trifleAddress);

        console.log(JSON.stringify(selectedNFT));
        const tx = new Transaction();
        const instruction = createCreateTrifleAccountInstruction({
            escrow: escrowAddress,
            metadata: selectedNFT.metadataAddress,
            mint: selectedNFT.address,
            tokenAccount: selectedNFTTokenAccountAddress,
            edition: selectedNFT.edition.address,
            trifleAccount: trifleAddress,
            trifleAuthority: wallet.publicKey,
            constraintModel: selectedEscrowConstraintModelAddress,
            payer: wallet.publicKey,
            tokenMetadataProgram: new PublicKey(TOKEN_METADATA_PROGRAM_ID),
            sysvarInstructions: SYSVAR_INSTRUCTIONS_PUBKEY,
        });

        try {
            tx.add(instruction);
            let sig = await wallet.sendTransaction(tx, connection, { skipPreflight: true })
            toast.success("Trifle account created");
            console.log(sig);
            window.location.href = `/trifle/${trifleAddress.toBase58()}`;
        } catch (e) {
            toast.error("Failed to create trifle account");
        }

    }

    const setSelectedModel = (input: any) => {
        setSelectedEscrowConstraintModel(input.target.value as string);
    }

    const createBaseNFT = async (updateAuthority: PublicKey) => {
        let nftMint = Keypair.generate();
        let trifleAddress = await findTriflePda(nftMint.publicKey, updateAuthority);
        let result;
        try {
            result = await metaplex!.nfts().create({
                uri: "https://shdw-drive.genesysgo.net/" + METAPLEX_BUCKET + "/" + trifleAddress[0].toString() + ".json",
                name: "test base  ",
                sellerFeeBasisPoints: 0,
                useNewMint: nftMint
            });
        } catch (e) {
            console.log(e);
        }

        handleCreateTrifleAccount(result?.nft);
    }

    return (
        <Container fixed>
            <Typography variant="h1">Token Owned Escrow</Typography>
            <Stack direction="column">
                <Stack direction="row" justifyContent="space-between">
                    <Typography variant="body1">
                        {selectedNFT ? `Selected NFT: ${selectedNFT.name}` : 'Select an NFT to become the base token'}
                    </Typography>
                    {selectedNFT ? <Button variant="contained" onClick={() => handleCreateTrifleAccount(selectedNFT)}>Create TOE</Button> : null}
                </Stack>
                <Select value={selectedEscrowConstraintModel} onChange={setSelectedModel}>
                    {Object.entries(escrowConstraintModels).map(([pubkey, ecm]) => {
                        console.log({ pubkey, ecm })
                        return <MenuItem key={ecm.name} value={pubkey}>{ecm.name}</MenuItem>
                    })}
                </Select>
            </Stack>
            {allNFTs.length > 0 && (<ImageList sx={{ width: 1120, height: 670 }} cols={5} rowHeight={220}>
                {allNFTs.map((nft) => (
                    <ImageListItem onClick={() => handleNFTClick(nft)} key={nft.address.toString()} sx={{ border: "1px solid red" }}>
                        <img
                            src={`${nft.json?.image}`}
                            alt={nft.json?.name}
                            loading="lazy"
                        />
                    </ImageListItem>
                ))}
            </ImageList>)}
            <Button variant="outlined" onClick={() => { if (wallet.publicKey) { createBaseNFT(wallet.publicKey); } }}>Create a Base NFT</Button>
        </Container >
    )
}

export default CreateTrifle 

