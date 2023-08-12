tests/ui/mir/mir_ascription_coercion.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// Tests that the result of type ascription has adjustments applied

#![feature(type_ascription)]

fn main() {
    let x = [1, 2, 3];
    // The RHS should coerce to &[i32]
    let _y : &[i32] = type_ascribe!(&x, &[i32; 3]);
}


