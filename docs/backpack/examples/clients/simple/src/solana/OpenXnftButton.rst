examples/clients/simple/src/solana/OpenXnftButton.tsx
=====================================================

Last edited: 2023-07-01 03:20:04

Contents:

.. code-block:: tsx

    import { PublicKey } from "@solana/web3.js";

export function OpenXnftButton() {
  const onClick = () => {
    const degodsXnft = "AM8TpkQaKnoiofQZrnBWhhbmUfrDo2kWJLLoNm2kybAW";
    window.backpack.openXnft(degodsXnft);
  };
  return <button onClick={onClick}>Open xNFT</button>;
}


