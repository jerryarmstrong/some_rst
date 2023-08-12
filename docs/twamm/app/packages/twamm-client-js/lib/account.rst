app/packages/twamm-client-js/lib/account.ts
===========================================

Last edited: 2023-07-21 18:33:07

Contents:

.. code-block:: ts

    import { Buffer } from "buffer";
import { encode } from "bs58";
import { sha256 } from "js-sha256";

export const getAccountDiscriminator = (name: string) =>
  Buffer.from(sha256.digest(`account:${name}`)).slice(0, 8);

export const getEncodedDiscriminator = (name: string) =>
  encode(getAccountDiscriminator(name));


