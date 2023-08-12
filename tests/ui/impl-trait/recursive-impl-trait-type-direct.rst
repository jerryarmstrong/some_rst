tests/ui/impl-trait/recursive-impl-trait-type-direct.rs
=======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

#![allow(unconditional_recursion)]

fn test() -> impl Sized {
    test()
}

fn main() {}


