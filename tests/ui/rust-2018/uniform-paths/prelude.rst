tests/ui/rust-2018/uniform-paths/prelude.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // build-pass (FIXME(62277): could be check-pass?)
// edition:2018

// Macro imported with `#[macro_use] extern crate`
use vec as imported_vec;

// Standard library prelude
use Vec as ImportedVec;

// Built-in type
use u8 as imported_u8;

// Built-in macro
use env as env_imported;

type A = imported_u8;

fn main() {
    imported_vec![0];
    ImportedVec::<u8>::new();
    env_imported!("PATH");
}


