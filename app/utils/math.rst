app/utils/math.ts
=================

Last edited: 2023-07-31 09:08:44

Contents:

.. code-block:: ts

    /**
 * Calculate a percentage using bigints, as numerator/denominator * 100
 * @returns the percentage, with the requested number of decimal places
 */
export function percentage(numerator: bigint, denominator: bigint, decimals: number): number {
    // since bigint is integer, we need to multiply first to get decimals
    // see https://stackoverflow.com/a/63095380/1375972
    const pow = 10 ** decimals;
    return Number(numerator * BigInt(100 * pow) / denominator) / pow;
}


