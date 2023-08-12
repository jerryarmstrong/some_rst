tests/ui/lint/dead-code/unused-variant-pub.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // build-pass
#![deny(unused)]

pub struct F;
pub struct B;

pub enum E {
    Foo(F),
    Bar(B),
}

fn main() {
    let _ = E::Foo(F);
}


