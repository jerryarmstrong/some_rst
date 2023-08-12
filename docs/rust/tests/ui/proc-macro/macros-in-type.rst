tests/ui/proc-macro/macros-in-type.rs
=====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
// aux-build:test-macros.rs

#[macro_use]
extern crate test_macros;

const C: identity!(u8) = 10;

fn main() {
    let c: u8 = C;
}


