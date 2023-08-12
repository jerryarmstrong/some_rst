stake-pool/js/src/utils/instruction.ts
======================================

Last edited: 2022-07-07 18:10:20

Contents:

.. code-block:: ts

    import * as BufferLayout from '@solana/buffer-layout';
import { Buffer } from 'buffer';

/**
 * @internal
 */
export type InstructionType = {
  /** The Instruction index (from solana upstream program) */
  index: number;
  /** The BufferLayout to use to build data */
  layout: BufferLayout.Layout<any>;
};

/**
 * Populate a buffer of instruction data using an InstructionType
 * @internal
 */
export function encodeData(type: InstructionType, fields?: any): Buffer {
  const allocLength = type.layout.span;
  const data = Buffer.alloc(allocLength);
  const layoutFields = Object.assign({ instruction: type.index }, fields);
  type.layout.encode(layoutFields, data);

  return data;
}

/**
 * Decode instruction data buffer using an InstructionType
 * @internal
 */
export function decodeData(type: InstructionType, buffer: Buffer): any {
  let data;
  try {
    data = type.layout.decode(buffer);
  } catch (err) {
    throw new Error('invalid instruction; ' + err);
  }

  if (data.instruction !== type.index) {
    throw new Error(
      `invalid instruction; instruction index mismatch ${data.instruction} != ${type.index}`,
    );
  }

  return data;
}


