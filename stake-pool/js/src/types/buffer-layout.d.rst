stake-pool/js/src/types/buffer-layout.d.ts
==========================================

Last edited: 2022-07-07 18:10:20

Contents:

.. code-block:: ts

    declare module 'buffer-layout' {
  export class Layout {}
  export class UInt {}
  /* eslint-disable  @typescript-eslint/no-unused-vars */
  export function struct<T>(fields: any, property?: string, decodePrefixes?: boolean): any;
  export function s32(property?: string): UInt;
  export function u32(property?: string): UInt;
  export function s16(property?: string): UInt;
  export function u16(property?: string): UInt;
  export function s8(property?: string): UInt;
  export function u8(property?: string): UInt;
}


