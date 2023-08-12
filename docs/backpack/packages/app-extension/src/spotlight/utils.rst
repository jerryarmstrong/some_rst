packages/app-extension/src/spotlight/utils.ts
=============================================

Last edited: 2023-07-01 03:20:04

Contents:

.. code-block:: ts

    export const getCurrentCounter = (
  arrowIndex: number,
  allResultsLength: number
) => {
  return arrowIndex >= 0
    ? arrowIndex % allResultsLength
    : (arrowIndex +
        -1 * Math.ceil(arrowIndex / allResultsLength) * allResultsLength) %
        allResultsLength;
};


