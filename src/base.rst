src/base.ts
===========

Last edited: 2022-03-24 14:12:32

Contents:

.. code-block:: ts

    import { Layout } from '@solana/buffer-layout';

export interface EncodeDecode<T> {
    decode(buffer: Buffer, offset?: number): T;
    encode(src: T, buffer: Buffer, offset?: number): number;
}

export const encodeDecode = <T>(layout: Layout<T>): EncodeDecode<T> => {
    const decode = layout.decode.bind(layout);
    const encode = layout.encode.bind(layout);
    return { decode, encode };
};


