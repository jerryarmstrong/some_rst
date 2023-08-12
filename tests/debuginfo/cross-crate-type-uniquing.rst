tests/debuginfo/cross-crate-type-uniquing.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // min-lldb-version: 310

// aux-build:cross_crate_debuginfo_type_uniquing.rs
extern crate cross_crate_debuginfo_type_uniquing;

// no-prefer-dynamic
// compile-flags:-g -C lto

pub struct C;
pub fn p() -> C {
    C
}

fn main() { }


