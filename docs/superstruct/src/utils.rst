src/utils.ts
============

Last edited: 2020-08-13 15:30:25

Contents:

.. code-block:: ts

    import { Struct, StructResult, StructFailure, StructContext } from './struct'

export type StructRecord<T> = Record<string, Struct<T>>
export type StructTuple<T> = { [K in keyof T]: Struct<T[K]> }

/**
 * Convert a validation result to an iterable of failures.
 */

export function toFailures(
  result: StructResult,
  context: StructContext
): Iterable<StructFailure> {
  if (result === true) {
    return []
  } else if (result === false) {
    return [context.fail()]
  } else {
    return result
  }
}


