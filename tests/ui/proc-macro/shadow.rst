tests/ui/proc-macro/shadow.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // aux-build:test-macros.rs

#[macro_use]
extern crate test_macros;
#[macro_use]
extern crate test_macros; //~ ERROR the name `test_macros` is defined multiple times

fn main() {}


