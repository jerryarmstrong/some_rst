hub/lib/image.ts
================

Last edited: 2023-08-11 18:13:34

Contents:

.. code-block:: ts

    export function getDimensions(src: string) {
  const image = new Image();

  return new Promise<{ height: number; width: number }>((res, rej) => {
    image.onload = () => {
      const height = image.height;
      const width = image.width;
      res({ height, width });
    };

    image.onerror = rej;
    image.src = src;
  });
}


