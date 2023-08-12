src/constants/modes.ts
======================

Last edited: 2023-05-04 20:47:44

Contents:

.. code-block:: ts

    import { Mode } from "../types";

interface Modes {
  [key: string]: Mode;
}

export default {
  numeric: "Numeric",
  alphanumeric: "Alphanumeric",
  byte: "Byte",
  kanji: "Kanji"
} as Modes;


