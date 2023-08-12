hub/lib/ntext.ts
================

Last edited: 2023-05-19 22:20:18

Contents:

.. code-block:: ts

    export function ntext(count: number, singular: string, plural?: string) {
  if (count === 1) {
    return singular;
  }

  return plural || `${singular}s`;
}


