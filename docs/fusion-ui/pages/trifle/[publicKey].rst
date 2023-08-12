pages/trifle/[publicKey].tsx
============================

Last edited: 2023-02-28 18:04:35

Contents:

.. code-block:: tsx

    /* eslint-disable @next/next/no-img-element */
import { useEffect, useState } from "react";
import type { NextPage } from 'next';
import { useRouter } from 'next/router';
import { Container, Typography, Select, MenuItem, Stack, ImageList, ImageListItem, Button } from "@mui/material";
import { useWallet, useConnection } from '@solana/wallet-adapter-react';
import { useMetaplex } from '../../hooks/useMetaplex';
import { toast } from 'react-toastify';
import { PublicKey, Transaction } from '@solana/web3.js';
import { Trifle, EscrowConstraintModel, createTransferInInstruction } from "@metaplex-foundation/mpl-trifle/dist/src/generated";
import { TokenOwnedEscrow, PROGRAM_ADDRESS as TOKEN_METADATA_PROGRAM_ID } from "@metaplex-foundation/mpl-token-metadata";
import { Nft, NftWithToken, Sft, SftWithToken } from "@metaplex-foundation/js";
import { loadNFTs } from "../../helpers/loadNFTs";
import { ASSOCIATED_TOKEN_PROGRAM_ID, getAssociatedTokenAddress, TOKEN_PROGRAM_ID } from "@solana/spl-token";

const TrifleDetail: NextPage = () => {
    const router = useRouter();
    const wallet = useWallet();
    const { connection } = useConnection();
    const { metaplex } = useMetaplex();
    const [trifle, setTrifle] = useState<Trifle | null>(null);
    const [escrowConstraintModel, setEscrowConstraintModel] = useState<EscrowConstraintModel | null>(null);
    const [escrow, setEscrow] = useState<TokenOwnedEscrow | null>(null);
    const [slots, setSlots] = useState<string[]>([]);
    const [baseToken, setBaseToken] = useState<Nft | null>()
    const [selectedSlot, setSelectedSlot] = useState<string | null>(null);
    const [allNFTs, setAllNFTs] = useState<(Nft | Sft | SftWithToken | NftWithToken)[]>([]);
    const [selectedNFT, setSelectedNFT] = useState<(Nft | Sft | SftWithToken | NftWithToken | null)>(null);
    const [time, setTime] = useState<number>(0);

    let { publicKey: trifleAddressString } = router.query;

    useEffect(() => {
        let interval = setInterval(() => setTime(Date.now()), 30000);

        if (!wallet.publicKey) {
            return;
        }
        if (!trifleAddressString) {
            return;
        }
        if (!metaplex) {
            return;
        }

        load().then(() => clearInterval(interval));
    // eslint-disable-next-line react-hooks/exhaustive-deps
    }, [trifleAddressString, metaplex, wallet.publicKey, time]);

    const load = async () => {
        console.log(trifleAddressString);
        let trifle = await loadTrifleAccount(new PublicKey(trifleAddressString as string));
        setTrifle(trifle!);

        console.log(trifle);
        let escrowConstraintModel = await loadEscrowConstraintModel(trifle!.escrowConstraintModel);
        setEscrowConstraintModel(escrowConstraintModel!);

        let escrow = await loadEscrow(trifle!.tokenEscrow);
        setEscrow(escrow!);
        console.log({ escrow })

        let slots = Array.from(escrowConstraintModel!.constraints.keys());
        setSlots(slots);

        // load the base token nft data
        let baseToken = await metaplex!.nfts().findByMint({ mintAddress: escrow!.baseToken });
        console.log(baseToken.address.toString());
        setBaseToken(baseToken as Nft);

        const nfts = await loadNFTs(metaplex!, wallet);

        setAllNFTs(nfts.filter((nft: any) => nft.address.toBase58() !== escrow!.baseToken.toBase58()));

        console.log({ trifle, escrowConstraintModel, escrow, slots, baseToken, nfts });

    }

    const loadTrifleAccount = async (trifleAddress: PublicKey): Promise<Trifle | undefined> => {
        let maybeTrifleAccount = await connection.getAccountInfo(trifleAddress);

        if (maybeTrifleAccount?.data) {
            return Trifle.fromAccountInfo(maybeTrifleAccount)[0];
        }
    };

    const loadEscrowConstraintModel = async (escrowConstraintModelAddress: PublicKey): Promise<EscrowConstraintModel | undefined> => {
        console.log(escrowConstraintModelAddress);
        let maybeEscrowConstraintModelAccount = await connection.getAccountInfo(escrowConstraintModelAddress);

        if (maybeEscrowConstraintModelAccount?.data) {
            return EscrowConstraintModel.fromAccountInfo(maybeEscrowConstraintModelAccount)[0];
        }
    }

    const loadEscrow = async (escrowAddress: PublicKey): Promise<TokenOwnedEscrow | undefined> => {
        let maybeEscrowAccount = await connection.getAccountInfo(escrowAddress);

        if (maybeEscrowAccount?.data) {
            return TokenOwnedEscrow.fromAccountInfo(maybeEscrowAccount)[0];
        }
    }

    const handleSlotChange = (e: any) => {
        setSelectedSlot(e.target.value as string);
    }

    const handleNFTClick = (nft: Nft | Sft | SftWithToken | NftWithToken) => {
        console.log({ nft });
        setSelectedNFT(nft);
    }

    const handleTransferClick = async () => {
        if (!selectedSlot) {
            toast.error('Please select a slot');
            return;
        }

        if (!selectedNFT) {
            toast.error('Please select an NFT');
            return;
        }

        let attributeDstAddress: PublicKey = await getAssociatedTokenAddress(selectedNFT.mint.address, trifle!.tokenEscrow, true);
        let attributeSrcAddress: PublicKey = await getAssociatedTokenAddress(selectedNFT.mint.address, wallet.publicKey!);
        let escrowTokenAccountAddress: PublicKey = await getAssociatedTokenAddress(escrow!.baseToken, trifle!.tokenEscrow, true);
        console.log(JSON.stringify({ trifle, escrowConstraintModel, escrow, selectedNFT, selectedSlot }));
        const tx = new Transaction();
        const instruction = createTransferInInstruction({
            trifle: new PublicKey(trifleAddressString as string),
            constraintModel: trifle!.escrowConstraintModel!,
            escrow: trifle!.tokenEscrow!,
            payer: wallet.publicKey!,
            trifleAuthority: wallet.publicKey!,
            escrowMint: baseToken!.address,
            escrowToken: escrowTokenAccountAddress,
            escrowEdition: baseToken!.edition.address,
            attributeMint: selectedNFT.address,
            attributeSrcToken: attributeSrcAddress,
            attributeDstToken: attributeDstAddress,
            attributeMetadata: selectedNFT.metadataAddress,
            splToken: TOKEN_PROGRAM_ID,
            splAssociatedTokenAccount: ASSOCIATED_TOKEN_PROGRAM_ID,
            tokenMetadataProgram: new PublicKey(TOKEN_METADATA_PROGRAM_ID)
        }, {
            transferInArgs: {
                slot: selectedSlot,
                amount: 1
            }
        });

        try {
            tx.add(instruction);
            let sig = await wallet.sendTransaction(tx, connection);
            toast.success("Transfer successful");
        } catch (e) {
            toast.error("Constraint violation");
        }

    }

    return <Container>
        <Stack direction={"column"} spacing={2}>
            <Typography variant="h1">Trifle</Typography>
            <Stack direction={"row"} justifyContent={"space-between"}>
                <Stack direction={"column"}>
                    {baseToken?.json?.image && <img key={Date.now()} alt={baseToken.json.image + "?" + Date.now()} src={baseToken.json.image + "?" + Date.now()} height={500} width={500} />}
                </Stack>
                <Stack direction={"column"} alignItems={"stretch"}>
                    <Typography variant={"h6"}>{selectedNFT?.json?.name || "Select an attribute NFT to transfer in"}</Typography>
                    <Stack direction={"row"} spacing={2}>
                        <Select value={selectedSlot} sx={{ width: "400px" }} onChange={handleSlotChange}>
                            {slots.map((slot) => <MenuItem key={slot} value={slot}>{slot}</MenuItem>)}
                        </Select>
                        <Button onClick={handleTransferClick} variant={"outlined"}>Transfer</Button>
                    </Stack>
                    <ImageList sx={{ width: 500, height: 500 }} cols={2} rowHeight={100}>
                        {allNFTs.map((nft) => <ImageListItem key={nft.address.toString()} onClick={() => handleNFTClick(nft)} >
                            <img src={nft.json?.image}
                                srcSet={nft.json?.image}
                                alt={nft.json?.name}
                                loading="lazy"
                            />
                        </ImageListItem>)}
                    </ImageList>
                </Stack>
            </Stack>
        </Stack>
    </Container>
}

export default TrifleDetail

