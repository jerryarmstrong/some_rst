tests/ui/const-generics/expose-default-substs-param-env.rs
==========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // build-pass

#![feature(generic_const_exprs)]
#![allow(unused_braces, incomplete_features)]

pub trait Foo<const N: usize> {}
pub trait Bar: Foo<{ 1 }> { }

fn main() {}


