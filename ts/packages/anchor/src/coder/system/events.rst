ts/packages/anchor/src/coder/system/events.ts
=============================================

Last edited: 2022-12-14 20:15:57

Contents:

.. code-block:: ts

    import { EventCoder } from "../index.js";
import { Idl } from "../../idl.js";
import { Event } from "../../program/event";
import { IdlEvent } from "../../idl";

export class SystemEventsCoder implements EventCoder {
  constructor(_idl: Idl) {}

  decode<E extends IdlEvent = IdlEvent, T = Record<string, string>>(
    _log: string
  ): Event<E, T> | null {
    throw new Error("System program does not have events");
  }
}


