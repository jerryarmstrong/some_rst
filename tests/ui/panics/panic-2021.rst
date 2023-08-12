tests/ui/panics/panic-2021.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // edition:2021

fn main() {
    panic!(123); //~ ERROR: format argument must be a string literal
    panic!("{}"); //~ ERROR: 1 positional argument in format string
    core::panic!("{}"); //~ ERROR: 1 positional argument in format string
    assert!(false, 123); //~ ERROR: format argument must be a string literal
    assert!(false, "{}"); //~ ERROR: 1 positional argument in format string
}


