packages/use-solana/src/index.ts
================================

Last edited: 2023-06-29 16:13:38

Contents:

.. code-block:: ts

    /**
 * [[include:use-solana/README.md]]
 * @module
 */

export * from "./adapters/index.js";
export * from "./context.js";
export * from "./error.js";
export * from "./hooks.js";
export * from "./providers.js";
export * from "./storage.js";
export * from "./utils/provider.js";
export * as icons from "@saberhq/wallet-adapter-icons";

// re-export solana utils
export * as solana from "@saberhq/solana-contrib";


