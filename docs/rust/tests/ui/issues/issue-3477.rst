tests/ui/issues/issue-3477.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let _p: char = 100;
    //~^ ERROR mismatched types
    //~| expected `char`, found `u8`
}


