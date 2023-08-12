packages/solana-contrib/src/error.ts
====================================

Last edited: 2023-06-29 16:13:38

Contents:

.. code-block:: ts

    export const firstAggregateError = (err: AggregateError) => {
  const errors = err.errors as Error[];
  const [firstError, ...remErrors] = [errors.pop(), ...errors];
  if (remErrors.length > 0) {
    console.error(remErrors);
  }
  return firstError;
};


