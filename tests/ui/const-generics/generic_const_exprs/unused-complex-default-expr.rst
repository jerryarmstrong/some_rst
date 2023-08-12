tests/ui/const-generics/generic_const_exprs/unused-complex-default-expr.rs
==========================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
#![feature(generic_const_exprs)]
#![allow(incomplete_features)]
struct Foo<const N: usize, const M: usize = { N + 1 }>;
struct Bar<const N: usize>(Foo<N, 3>);
fn main() {}


