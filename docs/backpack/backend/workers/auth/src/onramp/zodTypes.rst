backend/workers/auth/src/onramp/zodTypes.ts
===========================================

Last edited: 2023-07-01 03:20:04

Contents:

.. code-block:: ts

    import { Blockchain as BlockchainTy } from "@coral-xyz/common";
import { z } from "zod";

const ZodChain = z.enum(Object.values(BlockchainTy));
export type BlockChain = z.infer<typeof ZodChain>;

export const CreateSessionRequest = z.object({
  chain: ZodChain,
  publicKey: z.string(),
});


