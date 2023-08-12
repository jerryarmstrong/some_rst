tests/ui/const-generics/generic_const_exprs/assoc_const_unification/unifies_evaluatable.rs
==========================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

#![feature(generic_const_exprs)]
#![allow(incomplete_features)]

trait Trait {
    const ASSOC: usize;
}

fn foo<T: Trait, U: Trait>() where [(); T::ASSOC]:, {
    bar::<{ T::ASSOC }>();
}

fn bar<const N: usize>() -> [(); N] {
    [(); N]
}

fn main() {}


