utils/textToAddressList.ts
==========================

Last edited: 2023-05-19 22:20:18

Contents:

.. code-block:: ts

    import { validatePubkey } from '@utils/formValidation'

interface Addresses {
  valid: string[]
  invalid: string[]
}

export const textToAddressList = (textBlock: string): Addresses => {
  const valid: string[] = []
  const invalid: string[] = []

  textBlock.split(/[\s|,]/).forEach((address) => {
    if (validatePubkey(address)) {
      valid.push(address)
    } else if (address.trim() /* ignore empty strings */) {
      invalid.push(address.trim())
    }
  })

  return { valid, invalid }
}


