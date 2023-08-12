tests/ui/liveness/liveness-return-last-stmt-semi.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // regression test for #8005

macro_rules! test { () => { fn foo() -> i32 { 1; } } }
                                           //~^ ERROR mismatched types

fn no_return() -> i32 {} //~ ERROR mismatched types

fn bar(x: u32) -> u32 { //~ ERROR mismatched types
    x * 2;
}

fn baz(x: u64) -> u32 { //~ ERROR mismatched types
    x * 2;
}

fn main() {
    test!();
}


