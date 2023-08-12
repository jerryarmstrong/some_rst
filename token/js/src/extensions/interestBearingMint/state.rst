token/js/src/extensions/interestBearingMint/state.ts
====================================================

Last edited: 2022-07-07 18:10:20

Contents:

.. code-block:: ts

    import { s16, ns64, struct } from '@solana/buffer-layout';
import { publicKey } from '@solana/buffer-layout-utils';
import { PublicKey } from '@solana/web3.js';
import { Mint } from '../../state';
import { ExtensionType, getExtensionData } from '../extensionType';

export interface InterestBearingMintConfigState {
    rateAuthority: PublicKey;
    initializationTimestamp: BigInt;
    preUpdateAverageRate: number;
    lastUpdateTimestamp: BigInt;
    currentRate: number;
}

export const InterestBearingMintConfigStateLayout = struct<InterestBearingMintConfigState>([
    publicKey('rateAuthority'),
    ns64('initializationTimestamp'),
    s16('preUpdateAverageRate'),
    ns64('lastUpdateTimestamp'),
    s16('currentRate'),
]);

export const INTEREST_BEARING_MINT_CONFIG_STATE_SIZE = InterestBearingMintConfigStateLayout.span;

export function getInterestBearingMintConfigState(mint: Mint): InterestBearingMintConfigState | null {
    const extensionData = getExtensionData(ExtensionType.InterestBearingMint, mint.tlvData);
    if (extensionData !== null) {
        return InterestBearingMintConfigStateLayout.decode(extensionData);
    }
    return null;
}


