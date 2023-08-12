tests/ui/issues/issue-8761.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    enum Foo {
    A = 1i64,
    //~^ ERROR mismatched types
    //~| expected `isize`, found `i64`
    B = 2u8
    //~^ ERROR mismatched types
    //~| expected `isize`, found `u8`
}

fn main() {}


