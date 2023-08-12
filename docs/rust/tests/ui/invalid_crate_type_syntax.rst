tests/ui/invalid_crate_type_syntax.rs
=====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // regression test for issue 16974
#![crate_type(lib)]  //~ ERROR malformed `crate_type` attribute input

fn my_lib_fn() {}

fn main() {}


