ts/packages/spl-binary-oracle-pair/src/coder/events.ts
======================================================

Last edited: 2022-12-14 20:15:57

Contents:

.. code-block:: ts

    import { Idl, Event, EventCoder } from "@project-serum/anchor";
import { IdlEvent } from "@project-serum/anchor/dist/cjs/idl";

export class SplBinaryOraclePairEventsCoder implements EventCoder {
  constructor(_idl: Idl) {}

  decode<E extends IdlEvent = IdlEvent, T = Record<string, string>>(
    _log: string
  ): Event<E, T> | null {
    throw new Error("SplBinaryOraclePair program does not have events");
  }
}


