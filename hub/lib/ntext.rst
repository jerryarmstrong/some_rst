hub/lib/ntext.ts
================

Last edited: 2023-08-11 18:13:34

Contents:

.. code-block:: ts

    export function ntext(count: number, singular: string, plural?: string) {
  if (count === 1) {
    return singular;
  }

  return plural || `${singular}s`;
}


