clients/js/src/hooked/resolvers.ts
==================================

Last edited: 2023-08-12 00:00:44

Contents:

.. code-block:: ts

    import { MetadataArgsArgs } from '../generated';
import { hashMetadataCreators, hashMetadataData } from '../hash';

export const resolveDataHash = (
  context: any,
  accounts: any,
  args: { metadata: MetadataArgsArgs },
  programId: any,
  isWritable: boolean
): Uint8Array => hashMetadataData(args.metadata);

export const resolveCreatorHash = (
  context: any,
  accounts: any,
  args: { metadata: MetadataArgsArgs },
  programId: any,
  isWritable: boolean
): Uint8Array => hashMetadataCreators(args.metadata.creators);


