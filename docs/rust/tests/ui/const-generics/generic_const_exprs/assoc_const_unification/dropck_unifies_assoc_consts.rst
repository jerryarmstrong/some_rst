tests/ui/const-generics/generic_const_exprs/assoc_const_unification/dropck_unifies_assoc_consts.rs
==================================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
#![feature(generic_const_exprs)]
#![allow(incomplete_features)]

trait Trait {
    const ASSOC: usize;
}

struct Foo<T: Trait>(T)
where
    [(); T::ASSOC]:;

impl<T: Trait> Drop for Foo<T>
where
    [(); T::ASSOC]:,
{
    fn drop(&mut self) {}
}

fn main() {}


