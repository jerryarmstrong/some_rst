token/js/src/extensions/defaultAccountState/actions.ts
======================================================

Last edited: 2022-07-07 18:10:20

Contents:

.. code-block:: ts

    import {
    ConfirmOptions,
    Connection,
    PublicKey,
    sendAndConfirmTransaction,
    Signer,
    Transaction,
    TransactionSignature,
} from '@solana/web3.js';
import { TOKEN_2022_PROGRAM_ID } from '../../constants';
import { AccountState } from '../../state';
import {
    createInitializeDefaultAccountStateInstruction,
    createUpdateDefaultAccountStateInstruction,
} from './instructions';
import { getSigners } from '../../actions/internal';

/**
 * Initialize a default account state on a mint
 *
 * @param connection     Connection to use
 * @param payer          Payer of the transaction fees
 * @param mint        Mint to initialize with extension
 * @param state        Account state with which to initialize new accounts
 * @param confirmOptions Options for confirming the transaction
 * @param programId      SPL Token program account
 *
 * @return Signature of the confirmed transaction
 */
export async function initializeDefaultAccountState(
    connection: Connection,
    payer: Signer,
    mint: PublicKey,
    state: AccountState,
    confirmOptions?: ConfirmOptions,
    programId = TOKEN_2022_PROGRAM_ID
): Promise<TransactionSignature> {
    const transaction = new Transaction().add(createInitializeDefaultAccountStateInstruction(mint, state, programId));

    return await sendAndConfirmTransaction(connection, transaction, [payer], confirmOptions);
}

/**
 * Update the default account state on a mint
 *
 * @param connection     Connection to use
 * @param payer          Payer of the transaction fees
 * @param mint        Mint to modify
 * @param state        New account state to set on created accounts
 * @param freezeAuthority          Freeze authority of the mint
 * @param multiSigners   Signing accounts if `freezeAuthority` is a multisig
 * @param confirmOptions Options for confirming the transaction
 * @param programId      SPL Token program account
 *
 * @return Signature of the confirmed transaction
 */
export async function updateDefaultAccountState(
    connection: Connection,
    payer: Signer,
    mint: PublicKey,
    state: AccountState,
    freezeAuthority: Signer | PublicKey,
    multiSigners: Signer[] = [],
    confirmOptions?: ConfirmOptions,
    programId = TOKEN_2022_PROGRAM_ID
): Promise<TransactionSignature> {
    const [freezeAuthorityPublicKey, signers] = getSigners(freezeAuthority, multiSigners);

    const transaction = new Transaction().add(
        createUpdateDefaultAccountStateInstruction(mint, state, freezeAuthorityPublicKey, signers, programId)
    );

    return await sendAndConfirmTransaction(connection, transaction, [payer, ...signers], confirmOptions);
}


