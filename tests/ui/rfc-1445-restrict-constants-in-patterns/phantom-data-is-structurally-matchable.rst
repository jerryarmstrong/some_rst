tests/ui/rfc-1445-restrict-constants-in-patterns/phantom-data-is-structurally-matchable.rs
==========================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

// This file checks that `PhantomData` is considered structurally matchable.

use std::marker::PhantomData;

fn main() {
    let mut count = 0;

    // A type which is not structurally matchable:
    struct NotSM;

    // And one that is:
    #[derive(PartialEq, Eq)]
    struct SM;

    // Check that SM is structural-match:
    const CSM: SM = SM;
    match SM {
        CSM => count += 1,
    };

    // Check that PhantomData<T> is structural-match even if T is not.
    const CPD1: PhantomData<NotSM> = PhantomData;
    match PhantomData {
        CPD1 => count += 1,
    };

    // Check that PhantomData<T> is structural-match when T is.
    const CPD2: PhantomData<SM> = PhantomData;
    match PhantomData {
        CPD2 => count += 1,
    };

    // Check that a type which has a PhantomData is structural-match.
    #[derive(PartialEq, Eq, Default)]
    struct Foo {
        alpha: PhantomData<NotSM>,
        beta: PhantomData<SM>,
    }

    const CFOO: Foo = Foo {
        alpha: PhantomData,
        beta: PhantomData,
    };

    match Foo::default() {
        CFOO => count += 1,
    };

    // Final count must be 4 now if all
    assert_eq!(count, 4);
}


