components/EscrowConstraintForm.tsx
===================================

Last edited: 2023-02-28 18:04:35

Contents:

.. code-block:: tsx

    import { PublicKey } from "@solana/web3.js";
import { Checkbox, Select, TextField, Stack, Typography, Box, Button, MenuItem, FormControlLabel } from "@mui/material";
import { useState, createRef, FC } from "react";
import { ConstraintType } from "../helpers/constraintType";
import { toast } from "react-toastify";
import { TransferEffects } from "@metaplex-foundation/mpl-trifle/dist/src/transfer-effects";

type EscrowConstraintFormProps = {
    onSubmit: (name: string, tokenLimit: number, pubkeys: PublicKey[], constraintType: ConstraintType, transferEffects: number) => Promise<void>
}

const nameInputRef = createRef<HTMLInputElement>();
const pubkeyInputRef = createRef<HTMLInputElement>();
const tokenLimitRef = createRef<HTMLInputElement>();

export const EscrowConstraintForm: FC<EscrowConstraintFormProps> = ({ onSubmit }) => {
    const [selectedConstraintType, setSelectedConstraintType] = useState<ConstraintType>(ConstraintType.None);
    const [track, setTrack] = useState<boolean>(true);
    const [burn, setBurn] = useState<boolean>(false);
    const [freeze, setFreeze] = useState<boolean>(false);
    const [freezeParent, setFreezeParent] = useState<boolean>(false);

    const handleSubmit = async (e: any) => {
        e.preventDefault();
        const name = nameInputRef.current?.value as string;
        const tokenLimit = Number(tokenLimitRef.current?.value as string);
        const pubkeys = cleanPubkeys(pubkeyInputRef.current?.value as string || "");

        const transferEffects = new TransferEffects()
            .withTrack(track)
            .withBurn(burn)
            .withFreeze(freeze)
            .withFreezeParent(freezeParent)
            .toNumber();

        await onSubmit(name, tokenLimit, pubkeys, selectedConstraintType, transferEffects);
    }

    const cleanPubkeys = (input: string) => {
        const split = input.split(",")
            .map((s) => s.trim())
            .filter((s) => s.length > 0);

        try {
            return split.map(s => new PublicKey(s));
        } catch (e) {
            toast.error(`invalid pubkey${split.length > 1 ? "s" : ""}`);
            return [];
        }
    }

    const handleSelectedConstraintTypeChange = (e: any) => {
        setSelectedConstraintType(e.target.value);
    }

    const handleTrackCheckboxClick = (e: any) => {
        setTrack(e.target.checked);
    }
    const handleBurnCheckboxClick = (e: any) => {
        setBurn(e.target.checked);
    }
    const handleFreezeCheckboxClick = (e: any) => {
        setFreeze(e.target.checked);
    }
    const handleFreezeParentCheckboxClick = (e: any) => {
        setFreezeParent(e.target.checked);
    }

    return <Box component="form" noValidate autoComplete="off" onSubmit={handleSubmit}>
        <Stack direction="column" spacing={2}>
            <Typography>New Constraint Name</Typography>
            <TextField inputRef={nameInputRef} variant="outlined" name="Name" />
            <Typography>Token Limit</Typography>
            <TextField type="number" inputRef={tokenLimitRef} variant="outlined" name="TokenLimit" />
            <Typography>Constraint Type</Typography>
            <Select value={selectedConstraintType} onChange={handleSelectedConstraintTypeChange} name="Constraint Type">
                <MenuItem value={ConstraintType.None}>None</MenuItem>
                <MenuItem value={ConstraintType.Collection}>Collection</MenuItem>
                <MenuItem value={ConstraintType.Tokens}>Tokens</MenuItem>
            </Select>
            {selectedConstraintType === ConstraintType.None ? null : <>
                <Typography>Pubkey{selectedConstraintType === ConstraintType.Tokens ? "s" : null}</Typography>
                <TextField variant="outlined" name="Pubkey(s)" inputRef={pubkeyInputRef} />
            </>}
            <Typography>Transfer Effects</Typography>
            <Stack direction="row">
                <FormControlLabel control={<Checkbox checked={track} onChange={handleTrackCheckboxClick} />} label="Track" />
                <FormControlLabel control={<Checkbox checked={burn} onChange={handleBurnCheckboxClick} />} label="Burn" />
                <FormControlLabel control={<Checkbox checked={freeze} onChange={handleFreezeCheckboxClick} />} label="Freeze" />
                <FormControlLabel control={<Checkbox checked={freezeParent} onChange={handleFreezeParentCheckboxClick} />} label="Freeze Parent" />
            </Stack>
            <Button variant="outlined" type="submit">Submit</Button>
        </Stack>
    </Box >
}

export default EscrowConstraintForm;

