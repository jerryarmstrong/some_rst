packages/umi-serializers-encodings/src/nullCharacters.ts
========================================================

Last edited: 2023-07-27 15:49:41

Contents:

.. code-block:: ts

    /**
 * Removes null characters from a string.
 * @category Utils
 */
export const removeNullCharacters = (value: string) =>
  // eslint-disable-next-line no-control-regex
  value.replace(/\u0000/g, '');

/**
 * Pads a string with null characters at the end.
 * @category Utils
 */
export const padNullCharacters = (value: string, chars: number) =>
  value.padEnd(chars, '\u0000');


