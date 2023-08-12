tests/ui/feature-gates/feature-gate-type_ascription.rs
======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Type ascription is unstable

fn main() {
    let a = 10: u8; //~ ERROR type ascription is experimental
}


