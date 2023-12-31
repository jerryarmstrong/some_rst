hooks/useTotalTokenValue.ts
===========================

Last edited: 2023-05-19 22:20:18

Contents:

.. code-block:: ts

    import tokenPriceService from '@utils/services/tokenPrice'
import BigNumber from 'bignumber.js'
import { useEffect, useState } from 'react'

const useTotalTokenValue = ({
  amount,
  mintAddress,
}: {
  amount: number
  mintAddress: string
}) => {
  const [totalValue, setTotalValue] = useState('')

  useEffect(() => {
    const price = tokenPriceService.getUSDTokenPrice(mintAddress)
    const totalPrice = amount * price
    const totalPriceFormatted = amount
      ? new BigNumber(totalPrice).toFormat(0)
      : ''
    setTotalValue(totalPriceFormatted)
  }, [amount, mintAddress])

  return totalValue
}
export default useTotalTokenValue


