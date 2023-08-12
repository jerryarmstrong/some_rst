tests/ui/nll/projection-return.rs
=================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

#![feature(rustc_attrs)]

trait Foo {
    type Bar;
}

impl Foo for () {
    type Bar = u32;
}

fn foo() -> <() as Foo>::Bar {
    22
}

fn main() { }


