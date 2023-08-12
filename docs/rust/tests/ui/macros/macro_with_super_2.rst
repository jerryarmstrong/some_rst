tests/ui/macros/macro_with_super_2.rs
=====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// aux-build:macro_with_super_1.rs

// pretty-expanded FIXME #23616

#[macro_use]
extern crate macro_with_super_1;

declare!();

fn main() {
    bbb::ccc();
}


