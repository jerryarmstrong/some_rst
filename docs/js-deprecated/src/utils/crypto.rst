src/utils/crypto.ts
===================

Last edited: 2022-06-14 09:19:26

Contents:

.. code-block:: ts

    import { sha256 } from 'crypto-hash';
import { Buffer } from 'buffer';

export const getFileHash = async (file: Buffer) => Buffer.from(await sha256(file.toString()));


