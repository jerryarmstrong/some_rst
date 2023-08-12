examples/xnft/explorer/src/App/_atoms/solanaConnectionAtom.ts
=============================================================

Last edited: 2023-07-01 03:20:04

Contents:

.. code-block:: ts

    import { atom } from "recoil";
import { Connection } from "@solana/web3.js";
import ReactXnft, { SOLANA_CONNECT } from "react-xnft";

const solanaConnectionAtom = atom<boolean>({
  key: "solanaConnectionAtom",
  effects: [
    ({ setSelf }) => {
      setSelf(
        new Promise((resolve) => {
          let counter = 0;
          const interval = setInterval(() => {
            const connection = window?.xnft?.solana?.connection;

            if (connection) {
              clearInterval(interval);
              return resolve(true);
            }
            if (counter > 100) {
              clearInterval(interval);
              return resolve(false);
            }
            counter++;
          }, 100);
        })
      );
    },
  ],
});

export default solanaConnectionAtom;


