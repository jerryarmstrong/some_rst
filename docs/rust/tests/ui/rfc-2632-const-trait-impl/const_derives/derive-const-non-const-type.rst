tests/ui/rfc-2632-const-trait-impl/const_derives/derive-const-non-const-type.rs
===============================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(derive_const)]

pub struct A;

impl Default for A {
    fn default() -> A { A }
}

#[derive_const(Default)]
pub struct S(A);
//~^ cannot call non-const fn

fn main() {}


