tests/ui/const-generics/generic_const_exprs/auxiliary/anon_const_non_local.rs
=============================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(generic_const_exprs)]
#![allow(incomplete_features)]

pub struct Foo<const N: usize>;

pub fn foo<const N: usize>() -> Foo<{ N + 1 }> {
    Foo
}


