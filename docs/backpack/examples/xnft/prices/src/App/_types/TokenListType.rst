examples/xnft/prices/src/App/_types/TokenListType.ts
====================================================

Last edited: 2023-07-01 03:20:04

Contents:

.. code-block:: ts

    import { array, Infer } from "superstruct";
import { TokenInfoType } from "./TokenInfoType";

export type TokenListType = Infer<typeof TokenListType>;
export const TokenListType = array(TokenInfoType);


