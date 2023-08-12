app/components/account/nftoken/isNFTokenAccount.ts
==================================================

Last edited: 2023-07-31 09:08:44

Contents:

.. code-block:: ts

    import { PublicKey } from '@solana/web3.js';

import { Account } from '../../../providers/accounts';
import { NFTOKEN_ADDRESS } from './nftoken';
import { NftokenTypes } from './nftoken-types';

export function isNFTokenAccount(account: Account): boolean {
    return Boolean(account.owner.toBase58() === NFTOKEN_ADDRESS && account.data.raw);
}

const nftokenAccountDisc = 'IbRbNewPP2E=';

export const parseNFTokenNFTAccount = (account: Account): NftokenTypes.NftAccount | null => {
    if (!isNFTokenAccount(account)) {
        return null;
    }

    try {
        const parsed = NftokenTypes.nftAccountLayout.decode(account.data.raw!);

        if (!parsed) {
            return null;
        }

        if (Buffer.from(parsed!.discriminator).toString('base64') !== nftokenAccountDisc) {
            return null;
        }

        return {
            address: account.pubkey.toBase58(),
            authority: new PublicKey(parsed.authority).toBase58(),
            authority_can_update: Boolean(parsed.authority_can_update),
            collection: new PublicKey(parsed.collection).toBase58(),

            delegate: new PublicKey(parsed.delegate).toBase58(),
            holder: new PublicKey(parsed.holder).toBase58(),

            metadata_url: parsed.metadata_url?.replace(/\0/g, '') ?? null,
        };
    } catch (e) {
        console.error('Problem parsing NFToken NFT...', e);
        return null;
    }
};

const collectionAccountDisc = 'RQLwA3YS2fI=';
export const parseNFTokenCollectionAccount = (account: Account): NftokenTypes.CollectionAccount | null => {
    if (!isNFTokenAccount(account)) {
        return null;
    }

    try {
        const parsed = NftokenTypes.collectionAccountLayout.decode(account.data.raw!);

        if (!parsed) {
            return null;
        }
        if (Buffer.from(parsed.discriminator).toString('base64') !== collectionAccountDisc) {
            return null;
        }

        return {
            address: account.pubkey.toBase58(),
            authority: parsed.authority,
            authority_can_update: Boolean(parsed.authority_can_update),
            metadata_url: parsed.metadata_url?.replace(/\0/g, '') ?? null,
        };
    } catch (e) {
        console.error('Problem parsing NFToken Collection...', e);
        return null;
    }
};


