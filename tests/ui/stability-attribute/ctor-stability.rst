tests/ui/stability-attribute/ctor-stability.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // aux-build:ctor-stability.rs
// check-pass

extern crate ctor_stability;

fn main() {
    let _ = ctor_stability::Foo::A;
}


