packages/tamagui-core/src/components/BlockchainLogo.tsx
=======================================================

Last edited: 2023-07-01 03:20:04

Contents:

.. code-block:: tsx

    import { Image } from "react-native";
import type { Blockchain } from "@coral-xyz/common";
import { BLOCKCHAIN_COMMON } from "@coral-xyz/common";

function getBlockchainLogo(blockchain: Blockchain) {
  return BLOCKCHAIN_COMMON[blockchain].logoUri;
}

export function BlockchainLogo({
  size = 24,
  blockchain,
}: {
  size?: number;
  blockchain: Blockchain;
}) {
  const uri = getBlockchainLogo(blockchain);
  return <Image source={{ uri }} style={{ width: size, height: size }} />;
}


