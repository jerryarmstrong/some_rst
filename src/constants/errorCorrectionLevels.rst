src/constants/errorCorrectionLevels.ts
======================================

Last edited: 2023-05-04 20:47:44

Contents:

.. code-block:: ts

    import { ErrorCorrectionLevel } from "../types";

interface ErrorCorrectionLevels {
  [key: string]: ErrorCorrectionLevel;
}

export default {
  L: "L",
  M: "M",
  Q: "Q",
  H: "H"
} as ErrorCorrectionLevels;


