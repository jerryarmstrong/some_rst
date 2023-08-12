lib/utils.d.ts
==============

Last edited: 2020-08-13 15:30:25

Contents:

.. code-block:: ts

    import { Struct, StructResult, StructFailure, StructContext } from './struct';
export declare type StructRecord<T> = Record<string, Struct<T>>;
export declare type StructTuple<T> = {
    [K in keyof T]: Struct<T[K]>;
};
/**
 * Convert a validation result to an iterable of failures.
 */
export declare function toFailures(result: StructResult, context: StructContext): Iterable<StructFailure>;
//# sourceMappingURL=utils.d.ts.map

