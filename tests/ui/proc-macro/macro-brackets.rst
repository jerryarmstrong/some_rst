tests/ui/proc-macro/macro-brackets.rs
=====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // aux-build:test-macros.rs

#[macro_use]
extern crate test_macros;

macro_rules! id {
    ($($t:tt)*) => ($($t)*)
}

#[identity_attr]
id![static X: u32 = 'a';]; //~ ERROR: mismatched types


fn main() {}


