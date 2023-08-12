examples/xnft/explorer/src/App/_atoms/localStorageAtom.ts
=========================================================

Last edited: 2023-07-01 03:20:04

Contents:

.. code-block:: ts

    import { atomFamily } from "recoil";

const localStorageAtom = atomFamily<string | null, string>({
  key: "localStorageAtom",
  default: null,
  effects: (key) => [
    ({ setSelf, onSet }) => {
      setSelf(window?.xnft?.localStorage?.getItem(key) ?? null);

      onSet((newValue, _oldValue, isReset) => {
        if (newValue === null || isReset) {
          window?.xnft?.localStorage?.removeItem(key);
        }
        if (typeof newValue === "string") {
          window?.xnft?.localStorage?.setItem(key, newValue);
        }
      });
    },
  ],
});

export default localStorageAtom;


