hooks/useTreasuryInfo/calculateTotalValue.ts
============================================

Last edited: 2023-08-11 18:13:34

Contents:

.. code-block:: ts

    import { BigNumber } from 'bignumber.js'

export const calculateTotalValue = (values: BigNumber[]) => {
  let total = new BigNumber(0)

  for (const value of values.values()) {
    total = total.plus(value)
  }

  return total
}


