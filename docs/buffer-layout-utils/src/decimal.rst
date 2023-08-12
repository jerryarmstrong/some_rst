src/decimal.ts
==============

Last edited: 2022-03-24 14:12:32

Contents:

.. code-block:: ts

    import { Layout } from '@solana/buffer-layout';
import BigNumber from 'bignumber.js';
import { encodeDecode } from './base';
import { u128 } from './bigint';

export const WAD = new BigNumber('1e+18');

export const decimal = (property?: string): Layout<BigNumber> => {
    const layout = u128(property);
    const { encode, decode } = encodeDecode(layout);

    const decimalLayout = layout as Layout<unknown> as Layout<BigNumber>;

    decimalLayout.decode = (buffer: Buffer, offset: number) => {
        const src = decode(buffer, offset).toString();
        return new BigNumber(src).div(WAD);
    };

    decimalLayout.encode = (decimal: BigNumber, buffer: Buffer, offset: number) => {
        const src = BigInt(decimal.times(WAD).integerValue().toString());
        return encode(src, buffer, offset);
    };

    return decimalLayout;
};


