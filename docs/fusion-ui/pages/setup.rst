pages/setup.tsx
===============

Last edited: 2023-02-28 18:04:35

Contents:

.. code-block:: tsx

    import { useEffect, useState } from "react";
import type { NextPage } from "next";
import type { IdentitySigner } from "@metaplex-foundation/js";
import { token } from "@metaplex-foundation/js";
import { Box, Container, Stack, Typography, Button, List, ListItem } from "@mui/material";
import { PublicKey, Transaction } from "@solana/web3.js";
import { useConnection, useWallet } from "@solana/wallet-adapter-react";
import { useMetaplex } from "../hooks/useMetaplex";
import { toast } from "react-toastify";
import { TOKEN_PROGRAM_ID } from "@solana/spl-token";

export const Setup: NextPage = () => {
    const wallet = useWallet();
    const { connection } = useConnection();
    const { metaplex } = useMetaplex();
    const [collectionNFTMintAddress, setCollectionNFTMintAddress] = useState<PublicKey | undefined>(undefined);

    useEffect(() => {
        if (!wallet.publicKey) {
            return;
        }

        connection.getTokenAccountsByOwner(wallet.publicKey, { programId: TOKEN_PROGRAM_ID }).then(result => {
            console.log({ result });
        });
    }, [connection, wallet.publicKey]);

    const setupAttributeNFTs = async () => {
        if (!wallet.publicKey) {
            toast.error("wallet not connected");
            return;
        }

        if (!metaplex) {
            toast.error("metaplex not initialized");
            return;
        }

        await metaplex
            .nfts()
            .createSft({
                uri: "https://shdw-drive.genesysgo.net/G6yhKwkApJr1YCCmrusFibbsvrXZa4Q3GRThSHFiRJQW/Chain.json",
                name: "Test Dino Chain",
                sellerFeeBasisPoints: 500, // Represents 5.00%.
                tokenOwner: wallet.publicKey,
                tokenAmount: token(1),
            });

        await metaplex
            .nfts()
            .createSft({
                uri: "https://shdw-drive.genesysgo.net/G6yhKwkApJr1YCCmrusFibbsvrXZa4Q3GRThSHFiRJQW/Dragon_Breath.json",
                name: "Test Dino Dragon Breath",
                sellerFeeBasisPoints: 500, // Represents 5.00%.
                tokenOwner: wallet.publicKey,
                tokenAmount: token(1),
            });

        await metaplex
            .nfts()
            .createSft({
                uri: "https://shdw-drive.genesysgo.net/G6yhKwkApJr1YCCmrusFibbsvrXZa4Q3GRThSHFiRJQW/Piercing.json",
                name: "Test Dino Piercing",
                sellerFeeBasisPoints: 500, // Represents 5.00%.
                tokenOwner: wallet.publicKey,
                tokenAmount: token(1),
            });

        await metaplex
            .nfts()
            .createSft({
                uri: "https://shdw-drive.genesysgo.net/G6yhKwkApJr1YCCmrusFibbsvrXZa4Q3GRThSHFiRJQW/Base.json",
                name: "Test Dino Base",
                sellerFeeBasisPoints: 500, // Represents 5.00%.
                tokenOwner: wallet.publicKey,
                tokenAmount: token(1),
            });


        // // the base token
        // await metaplex.nfts().create({
        //     uri: "https://shdw-drive.genesysgo.net/G6yhKwkApJr1YCCmrusFibbsvrXZa4Q3GRThSHFiRJQW/Combined.json",
        //     name: "Test Dino",
        //     sellerFeeBasisPoints: 500, // Represents 5.00%.
        //     tokenOwner: wallet.publicKey,
        // });

    }

    const setupCollectionNFT = async () => {
        const result = await metaplex!.nfts().create({
            uri: "https://shdw-drive.genesysgo.net/G6yhKwkApJr1YCCmrusFibbsvrXZa4Q3GRThSHFiRJQW/Collection.json",
            name: "test collection  ",
            sellerFeeBasisPoints: 0,
            isCollection: true,
            collectionIsSized: true
        });

        setCollectionNFTMintAddress(result.mintAddress);
    }

    return <Container fixed>
        <Typography variant="h1">Setup</Typography>
        <Typography variant="subtitle1">Create attribute NFTs to use use with a TOE</Typography>
        <Box sx={{ marginTop: 8 }}>
            <Stack direction="column" spacing={2}>
                <Button variant="outlined" onClick={setupAttributeNFTs}>Create Attribute NFTs</Button>
                <Button variant="outlined" onClick={setupCollectionNFT}>Create a Collection NFT</Button>
                {collectionNFTMintAddress && <Typography>{collectionNFTMintAddress.toString()}</Typography>}
            </Stack>
        </Box>
    </Container>
}

export default Setup

