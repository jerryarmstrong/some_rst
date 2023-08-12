packages/recoil/src/hooks/transaction-request.tsx
=================================================

Last edited: 2023-07-01 03:20:04

Contents:

.. code-block:: tsx

    import { useRecoilState } from "recoil";

import * as atoms from "../atoms";
import type { TransactionRequest } from "../atoms/transaction-request";

export function useTransactionRequest(): [
  TransactionRequest | undefined,
  (tx: TransactionRequest | undefined) => void
] {
  return useRecoilState(atoms.transactionRequest);
}


