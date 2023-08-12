packages/recoil/src/hooks/keyring.tsx
=====================================

Last edited: 2023-07-01 03:20:04

Contents:

.. code-block:: tsx

    import type { KeyringStoreState } from "@coral-xyz/secure-background/types";
import { useRecoilValue } from "recoil";

import * as atoms from "../atoms";

export function useKeyringStoreState(): KeyringStoreState {
  return useRecoilValue(atoms.keyringStoreState)!;
}

export function useKeyringHasMnemonic(): boolean {
  return useRecoilValue(atoms.keyringHasMnemonic);
}


