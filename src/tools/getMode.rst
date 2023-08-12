src/tools/getMode.ts
====================

Last edited: 2023-05-04 20:47:44

Contents:

.. code-block:: ts

    import modes from "../constants/modes";
import { Mode } from "../types";

export default function getMode(data: string): Mode {
  switch (true) {
    case /^[0-9]*$/.test(data):
      return modes.numeric;
    case /^[0-9A-Z $%*+\-./:]*$/.test(data):
      return modes.alphanumeric;
    default:
      return modes.byte;
  }
}


