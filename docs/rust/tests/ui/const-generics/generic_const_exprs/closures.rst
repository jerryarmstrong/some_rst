tests/ui/const-generics/generic_const_exprs/closures.rs
=======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(generic_const_exprs)]
#![allow(incomplete_features)]
fn test<const N: usize>() -> [u8; N + (|| 42)()] {}
//~^ ERROR cycle detected when building an abstract representation

fn main() {}


