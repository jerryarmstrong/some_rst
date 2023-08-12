src/hooks/useTokenName.ts
=========================

Last edited: 2021-03-16 20:45:52

Contents:

.. code-block:: ts

    import { PublicKey } from "@solana/web3.js";
import { useConnectionConfig } from "../contexts/connection";
import { getTokenName } from "../utils/utils";

export function useTokenName(mintAddress?: string | PublicKey) {
  const { tokenMap } = useConnectionConfig();
  const address =
    typeof mintAddress === "string" ? mintAddress : mintAddress?.toBase58();
  return getTokenName(tokenMap, address);
}


