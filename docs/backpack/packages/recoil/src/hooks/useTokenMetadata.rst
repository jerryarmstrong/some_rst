packages/recoil/src/hooks/useTokenMetadata.tsx
==============================================

Last edited: 2023-07-01 03:20:04

Contents:

.. code-block:: tsx

    import type { Blockchain } from "@coral-xyz/common";
import { useRecoilValue } from "recoil";

import { tokenMetadata } from "../atoms/tokenMetadata";

export const useTokenMetadata = ({
  mintAddress,
  blockchain,
}: {
  mintAddress: string;
  blockchain: Blockchain;
}) => {
  return useRecoilValue(tokenMetadata({ mintAddress, blockchain }));
};


