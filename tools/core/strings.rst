tools/core/strings.ts
=====================

Last edited: 2023-08-11 18:13:34

Contents:

.. code-block:: ts

    export function equalsIgnoreCase(
  str1: string | undefined,
  str2: string | undefined
) {
  return str1?.toUpperCase() === str2?.toUpperCase()
}


