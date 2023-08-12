app/core/shortvec-encoding.ts
=============================

Last edited: 2020-09-01 18:17:54

Contents:

.. code-block:: ts

    export const decodeLength = (bytes: Array<number>): number => {
  let len = 0
  let size = 0
  for (; ;) {
    let elem = bytes.shift()
    // @ts-ignore
    len |= (elem & 0x7f) << (size * 7)
    size += 1
    // @ts-ignore
    if ((elem & 0x80) === 0) {
      break
    }
  }
  return len
}

export const encodeLength = (bytes: Array<number>, len: number): void => {
  let rem_len = len
  for (; ;) {
    let elem = rem_len & 0x7f
    rem_len >>= 7
    if (rem_len === 0) {
      bytes.push(elem)
      break
    } else {
      elem |= 0x80
      bytes.push(elem)
    }
  }
}


