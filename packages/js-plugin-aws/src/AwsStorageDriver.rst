packages/js-plugin-aws/src/AwsStorageDriver.ts
==============================================

Last edited: 2023-05-26 09:49:40

Contents:

.. code-block:: ts

    import { S3Client, PutObjectCommand } from '@aws-sdk/client-s3';
import {
  MetaplexFile,
  StorageDriver,
  lamports,
  Amount,
} from '@metaplex-foundation/js';

export class AwsStorageDriver implements StorageDriver {
  protected client: S3Client;
  protected bucketName: string;

  constructor(client: S3Client, bucketName: string) {
    this.client = client;
    this.bucketName = bucketName;
  }

  async getUploadPrice(): Promise<Amount> {
    return lamports(0);
  }

  async upload(file: MetaplexFile): Promise<string> {
    const command = new PutObjectCommand({
      Bucket: this.bucketName,
      Key: file.uniqueName,
      Body: file.buffer,
      ContentType: file.contentType || undefined,
    });

    try {
      await this.client.send(command);

      return await this.getUrl(file.uniqueName);
    } catch (err) {
      // TODO: Custom errors.
      throw err;
    }
  }

  async getUrl(key: string) {
    const region = await this.client.config.region();
    const encodedKey = encodeURIComponent(key);

    return `https://s3.${region}.amazonaws.com/${this.bucketName}/${encodedKey}`;
  }
}


