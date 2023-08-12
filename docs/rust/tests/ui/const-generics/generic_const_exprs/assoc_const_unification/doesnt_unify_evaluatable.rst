tests/ui/const-generics/generic_const_exprs/assoc_const_unification/doesnt_unify_evaluatable.rs
===============================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(generic_const_exprs)]
#![allow(incomplete_features)]

trait Trait {
    const ASSOC: usize;
}

fn foo<T: Trait, U: Trait>() where [(); U::ASSOC]:, {
    bar::<{ T::ASSOC }>();
    //~^ ERROR: unconstrained generic constant
}

fn bar<const N: usize>() {}

fn main() {}


