examples/xnft/explorer/src/App/_types/XnftAccount.ts
====================================================

Last edited: 2023-07-01 03:20:04

Contents:

.. code-block:: ts

    import { type Xnft } from "../_utils/xnftIDL";
import { type IdlAccounts } from "@project-serum/anchor";

type XnftAccount = IdlAccounts<Xnft>["xnft"];

export default XnftAccount;


