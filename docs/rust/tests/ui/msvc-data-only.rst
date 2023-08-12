tests/ui/msvc-data-only.rs
==========================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// aux-build:msvc-data-only-lib.rs

extern crate msvc_data_only_lib;

fn main() {
    println!("The answer is {} !", msvc_data_only_lib::FOO);
}


