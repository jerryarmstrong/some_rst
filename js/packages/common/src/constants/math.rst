js/packages/common/src/constants/math.ts
========================================

Last edited: 2022-06-29 06:18:54

Contents:

.. code-block:: ts

    import BN from 'bn.js';

export const TEN = new BN(10);
export const HALF_WAD = TEN.pow(new BN(18));
export const WAD = TEN.pow(new BN(18));
export const RAY = TEN.pow(new BN(27));
export const ZERO = new BN(0);


