packages/umi-serializers-numbers/src/errors.ts
==============================================

Last edited: 2023-07-27 15:49:41

Contents:

.. code-block:: ts

    /** @category Errors */
export class NumberOutOfRangeError extends RangeError {
  readonly name: string = 'NumberOutOfRangeError';

  constructor(
    serializer: string,
    min: number | bigint,
    max: number | bigint,
    actual: number | bigint
  ) {
    super(
      `Serializer [${serializer}] expected number to be between ${min} and ${max}, got ${actual}.`
    );
  }
}


