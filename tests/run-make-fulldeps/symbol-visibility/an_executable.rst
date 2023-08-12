tests/run-make-fulldeps/symbol-visibility/an_executable.rs
==========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_type="bin"]

extern crate an_rlib;

pub fn public_rust_function_from_exe() {}

fn main() {}


