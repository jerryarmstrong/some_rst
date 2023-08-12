token/js/src/extensions/memoTransfer/actions.ts
===============================================

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
import {
    createEnableRequiredMemoTransfersInstruction,
    createDisableRequiredMemoTransfersInstruction,
} from './instructions';
import { getSigners } from '../../actions/internal';

/**
 * Enable memo transfers on the given account
 *
 * @param connection     Connection to use
 * @param payer          Payer of the transaction fees
 * @param account        Account to modify
 * @param owner          Owner of the account
 * @param multiSigners   Signing accounts if `owner` is a multisig
 * @param confirmOptions Options for confirming the transaction
 * @param programId      SPL Token program account
 *
 * @return Signature of the confirmed transaction
 */
export async function enableRequiredMemoTransfers(
    connection: Connection,
    payer: Signer,
    account: PublicKey,
    owner: Signer | PublicKey,
    multiSigners: Signer[] = [],
    confirmOptions?: ConfirmOptions,
    programId = TOKEN_2022_PROGRAM_ID
): Promise<TransactionSignature> {
    const [ownerPublicKey, signers] = getSigners(owner, multiSigners);

    const transaction = new Transaction().add(
        createEnableRequiredMemoTransfersInstruction(account, ownerPublicKey, signers, programId)
    );

    return await sendAndConfirmTransaction(connection, transaction, [payer, ...signers], confirmOptions);
}

/**
 * Disable memo transfers on the given account
 *
 * @param connection     Connection to use
 * @param payer          Payer of the transaction fees
 * @param account        Account to modify
 * @param owner          Owner of the account
 * @param multiSigners   Signing accounts if `owner` is a multisig
 * @param confirmOptions Options for confirming the transaction
 * @param programId      SPL Token program account
 *
 * @return Signature of the confirmed transaction
 */
export async function disableRequiredMemoTransfers(
    connection: Connection,
    payer: Signer,
    account: PublicKey,
    owner: Signer | PublicKey,
    multiSigners: Signer[] = [],
    confirmOptions?: ConfirmOptions,
    programId = TOKEN_2022_PROGRAM_ID
): Promise<TransactionSignature> {
    const [ownerPublicKey, signers] = getSigners(owner, multiSigners);

    const transaction = new Transaction().add(
        createDisableRequiredMemoTransfersInstruction(account, ownerPublicKey, signers, programId)
    );

    return await sendAndConfirmTransaction(connection, transaction, [payer, ...signers], confirmOptions);
}


