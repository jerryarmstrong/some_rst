tests/ui/recursion_limit/zero.rs
================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test that a `limit` of 0 is valid

#![recursion_limit = "0"]

macro_rules! test {
    () => {};
    ($tt:tt) => { test!(); };
}

test!(test); //~ ERROR recursion limit reached while expanding `test!`

fn main() {}


