src/tools/miri/tests/fail/validity/ref_to_uninhabited2.rs
=========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use std::mem::transmute;

enum Void {}

fn main() {
    unsafe {
        let _x: &(i32, Void) = transmute(&42); //~ERROR: encountered a reference pointing to uninhabited type (i32, Void)
    }
}


