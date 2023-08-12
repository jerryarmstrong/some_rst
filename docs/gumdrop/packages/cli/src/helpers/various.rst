packages/cli/src/helpers/various.ts
===================================

Last edited: 2022-08-25 19:21:42

Contents:

.. code-block:: ts

    export const getUnixTs = () => {
  return new Date().getTime() / 1000;
};

export function sleep(ms: number): Promise<void> {
  return new Promise(resolve => setTimeout(resolve, ms));
}


