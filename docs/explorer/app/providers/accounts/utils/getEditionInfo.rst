app/providers/accounts/utils/getEditionInfo.ts
==============================================

Last edited: 2023-07-31 09:08:44

Contents:

.. code-block:: ts

    import { programs } from '@metaplex/js';
import { Connection } from '@solana/web3.js';

const {
    metadata: { Metadata, MasterEdition, MetadataKey },
} = programs;

type MasterEditionData = programs.metadata.MasterEditionV1Data | programs.metadata.MasterEditionV2Data;
type EditionData = programs.metadata.EditionData;

export type EditionInfo = {
    masterEdition?: MasterEditionData;
    edition?: EditionData;
};

export default async function getEditionInfo(
    metadata: programs.metadata.Metadata,
    connection: Connection
): Promise<EditionInfo> {
    try {
        const edition = (await Metadata.getEdition(connection, metadata.data.mint)).data;

        if (edition) {
            if (edition.key === MetadataKey.MasterEditionV1 || edition.key === MetadataKey.MasterEditionV2) {
                return {
                    edition: undefined,
                    masterEdition: edition as MasterEditionData,
                };
            }

            // This is an Edition NFT. Pull the Parent (MasterEdition)
            const masterEdition = (await MasterEdition.load(connection, (edition as EditionData).parent)).data;
            if (masterEdition) {
                return {
                    edition: edition as EditionData,
                    masterEdition,
                };
            }
        }
    } catch {
        /* ignore */
    }

    return {
        edition: undefined,
        masterEdition: undefined,
    };
}


