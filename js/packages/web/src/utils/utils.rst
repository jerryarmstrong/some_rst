js/packages/web/src/utils/utils.ts
==================================

Last edited: 2022-06-29 06:18:54

Contents:

.. code-block:: ts

    export const cleanName = (name?: string): string | undefined => {
  if (!name) {
    return undefined;
  }

  return name.replace(/\s+/g, '-');
};

export const getLast = <T>(arr: T[]) => {
  if (arr.length <= 0) {
    return undefined;
  }

  return arr[arr.length - 1];
};


