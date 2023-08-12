app/providers/accounts/utils/isMetaplexNFT.ts
=============================================

Last edited: 2023-07-31 09:08:44

Contents:

.. code-block:: ts

    import { MintAccountInfo } from '@validators/accounts/token';

import { ParsedData, TokenProgramData } from '..';

export default function isMetaplexNFT(
    parsedData?: ParsedData,
    mintInfo?: MintAccountInfo
): parsedData is TokenProgramData {
    return !!(
        parsedData?.program === 'spl-token' &&
        parsedData?.parsed.type === 'mint' &&
        parsedData?.nftData &&
        mintInfo?.decimals === 0 &&
        (parseInt(mintInfo.supply) === 1 || parsedData?.nftData.metadata.tokenStandard === 1)
    );
}


