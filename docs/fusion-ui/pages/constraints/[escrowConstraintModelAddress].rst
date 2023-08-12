pages/constraints/[escrowConstraintModelAddress].tsx
====================================================

Last edited: 2023-02-28 18:04:35

Contents:

.. code-block:: tsx

    import { useEffect, useState } from "react";
import { PublicKey, Transaction, SYSVAR_INSTRUCTIONS_PUBKEY } from "@solana/web3.js";
import { toast } from "react-toastify";
import { useWallet, useConnection } from "@solana/wallet-adapter-react";
import type { NextPage } from "next";
import { useRouter } from "next/router";
import { Container, Typography, Stack, Button, List, ListItem } from "@mui/material";
import { EscrowConstraintModel, EscrowConstraint, createAddNoneConstraintToEscrowConstraintModelInstruction, createAddCollectionConstraintToEscrowConstraintModelInstruction, createAddTokensConstraintToEscrowConstraintModelInstruction } from "@metaplex-foundation/mpl-trifle/dist/src/generated";
import { EscrowConstraintForm } from "../../components/EscrowConstraintForm";
import { ConstraintType } from "../../helpers/constraintType";
import { findMetadataPda } from "@metaplex-foundation/js";

const ConstraintDetail: NextPage = () => {
    const router = useRouter();
    const { connection } = useConnection();
    const wallet = useWallet();
    const { escrowConstraintModelAddress } = router.query;
    const [escrowConstraintModel, setEscrowConstraintModel] = useState<EscrowConstraintModel | null>(null);
    const [showConstraintForm, setShowConstraintForm] = useState(false);

    useEffect(() => {
        const load = async () => {
            if (!escrowConstraintModelAddress) {
                return;
            }
            const maybeEscrowConstraintModel = await loadEscrowConstraintModel(new PublicKey(escrowConstraintModelAddress));
            console.log("escrow constraint model", maybeEscrowConstraintModel);
            setEscrowConstraintModel(maybeEscrowConstraintModel);
        }

        load().then(() => {
            console.log("loaded");
        });

    // eslint-disable-next-line react-hooks/exhaustive-deps
    }, [escrowConstraintModelAddress])

    const loadEscrowConstraintModel = async (address: PublicKey): Promise<EscrowConstraintModel | null> => {
        const maybeEscrowConstraintModel = await connection.getAccountInfo(address);
        if (maybeEscrowConstraintModel?.data) {
            return EscrowConstraintModel.fromAccountInfo(maybeEscrowConstraintModel)[0];
        }
        return null;
    }

    const handleAddConstraintClick = async () => {
        setShowConstraintForm(true);
    }

    const handleConstraintFormSubmit = async (name: string, tokenLimit: number, tokens: PublicKey[], constraintType: ConstraintType, transferEffects: number) => {
        if (!wallet.publicKey) {
            toast.error("wallet disconnected");
            return;
        }

        let tx = new Transaction();
        const escrowConstraintModel = new PublicKey(escrowConstraintModelAddress as string);

        switch (constraintType) {
            case ConstraintType.None:
                tx.add(createAddNoneConstraintToEscrowConstraintModelInstruction({
                    constraintModel: escrowConstraintModel,
                    payer: wallet.publicKey,
                    updateAuthority: wallet.publicKey,
                    sysvarInstructions: SYSVAR_INSTRUCTIONS_PUBKEY,
                }, {
                    addNoneConstraintToEscrowConstraintModelArgs: { constraintName: name, tokenLimit, transferEffects }
                }));
                break;
            case ConstraintType.Collection:
                let [mint] = tokens;
                let metadataAddress = findMetadataPda(mint);
                tx.add(createAddCollectionConstraintToEscrowConstraintModelInstruction({
                    constraintModel: escrowConstraintModel,
                    payer: wallet.publicKey,
                    updateAuthority: wallet.publicKey,
                    collectionMint: mint,
                    collectionMintMetadata: metadataAddress,
                    sysvarInstructions: SYSVAR_INSTRUCTIONS_PUBKEY,
                }, {
                    addCollectionConstraintToEscrowConstraintModelArgs: { constraintName: name, tokenLimit, transferEffects }
                }));
                break;
            case ConstraintType.Tokens:
                tx.add(createAddTokensConstraintToEscrowConstraintModelInstruction({
                    constraintModel: escrowConstraintModel,
                    payer: wallet.publicKey,
                    updateAuthority: wallet.publicKey,
                    sysvarInstructions: SYSVAR_INSTRUCTIONS_PUBKEY,
                }, {
                    addTokensConstraintToEscrowConstraintModelArgs: { constraintName: name, tokenLimit, tokens, transferEffects }
                }))
                break;
            default:
                console.log("reached impossible default case");
        }

        let sig = await wallet.sendTransaction(tx, connection)

        // TODO: reset form and reload constraint model.
        await connection.confirmTransaction(sig);
        setShowConstraintForm(false);
        setEscrowConstraintModel(await loadEscrowConstraintModel(escrowConstraintModel));
    }

    return (
        <Container>
            <Typography variant="subtitle1">Escrow Constraint Model</Typography>
            <Typography variant="h1">{escrowConstraintModel?.name}</Typography>
            <Stack>
                <List>
                    {escrowConstraintModel ? Array.from(escrowConstraintModel.constraints.entries()).map(data => {
                        let [name, constraint] = data;
                        // constraint component goes here.
                        return (
                            <div key={name}>{name}</div>
                        )
                    }) : null}
                </List>
                {!showConstraintForm ? <Button variant="outlined" onClick={handleAddConstraintClick}>Add a Constraint</Button> : null}
                {showConstraintForm ? <EscrowConstraintForm onSubmit={handleConstraintFormSubmit} /> : null}
            </Stack>
        </Container>);
}

export default ConstraintDetail;

