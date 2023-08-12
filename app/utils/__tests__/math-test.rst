app/utils/__tests__/math-test.ts
================================

Last edited: 2023-07-31 09:08:44

Contents:

.. code-block:: ts

    import { percentage } from '@utils/math';

describe('percentage', () => {
  it('returns a number with the right decimals', () => {
    expect(percentage(BigInt(1), BigInt(3), 0)).toEqual(33)
    expect(percentage(BigInt(1), BigInt(3), 1)).toEqual(33.3)
    expect(percentage(BigInt(1), BigInt(3), 2)).toEqual(33.33)
  });
});


