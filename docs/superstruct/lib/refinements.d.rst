lib/refinements.d.ts
====================

Last edited: 2020-08-13 15:30:25

Contents:

.. code-block:: ts

    import { Struct } from './struct';
/**
 * Augment a string or array struct to constrain its length to zero.
 */
export declare function empty<T extends string | any[]>(S: Struct<T>): Struct<T>;
/**
 * Augment a string or array struct to constrain its length to being between a
 * minimum and maximum size.
 */
export declare function length<T extends string | any[]>(S: Struct<T>, min: number, max: number): Struct<T>;
/**
 * Refine a string struct to match a specific regexp pattern.
 */
export declare function pattern<T extends string>(S: Struct<T>, regexp: RegExp): Struct<T>;
/**
 * Augment a `Struct` to add an additional refinement to the validation.
 */
export declare function refinement<T>(struct: Struct<T>, type: string, refiner: Struct<T>['refiner']): Struct<T>;
//# sourceMappingURL=refinements.d.ts.map

