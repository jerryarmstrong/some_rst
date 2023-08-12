packages/js-plugin-aws/src/plugin.ts
====================================

Last edited: 2023-05-26 09:49:40

Contents:

.. code-block:: ts

    import type { S3Client } from '@aws-sdk/client-s3';
import type { Metaplex, MetaplexPlugin } from '@metaplex-foundation/js';
import { AwsStorageDriver } from './AwsStorageDriver';

export const awsStorage = (
  client: S3Client,
  bucketName: string
): MetaplexPlugin => ({
  install(metaplex: Metaplex) {
    metaplex.storage().setDriver(new AwsStorageDriver(client, bucketName));
  },
});


