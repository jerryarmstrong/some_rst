tests/ui/consts/array-literal-index-oob.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // build-pass
// ignore-pass (test emits codegen-time warnings and verifies that they are not errors)

#![warn(unconditional_panic)]

fn main() {
    &{ [1, 2, 3][4] };
    //~^ WARN operation will panic
}


