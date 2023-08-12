js/packages/common/src/utils/isValidHttpUrl.ts
==============================================

Last edited: 2022-06-29 06:18:54

Contents:

.. code-block:: ts

    export function isValidHttpUrl(text: string) {
  if (text.startsWith('http:') || text.startsWith('https:')) {
    return true;
  }

  return false;
}


