tests/ui/crate-loading/cross-compiled-proc-macro.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // edition:2018
// compile-flags:--extern reproduction
// aux-build:proc-macro.rs
// check-pass

reproduction::mac!();

fn main() {}


