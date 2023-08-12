packages/library-legacy/src/utils/borsh-schema.ts
=================================================

Last edited: 2023-08-11 09:49:26

Contents:

.. code-block:: ts

    import {Buffer} from 'buffer';
import {serialize, deserialize, deserializeUnchecked} from 'borsh';

// Class wrapping a plain object
export class Struct {
  constructor(properties: any) {
    Object.assign(this, properties);
  }

  encode(): Buffer {
    return Buffer.from(serialize(SOLANA_SCHEMA, this));
  }

  static decode(data: Buffer): any {
    return deserialize(SOLANA_SCHEMA, this, data);
  }

  static decodeUnchecked(data: Buffer): any {
    return deserializeUnchecked(SOLANA_SCHEMA, this, data);
  }
}

// Class representing a Rust-compatible enum, since enums are only strings or
// numbers in pure JS
export class Enum extends Struct {
  enum: string = '';
  constructor(properties: any) {
    super(properties);
    if (Object.keys(properties).length !== 1) {
      throw new Error('Enum can only take single value');
    }
    Object.keys(properties).map(key => {
      this.enum = key;
    });
  }
}

export const SOLANA_SCHEMA: Map<Function, any> = new Map();


