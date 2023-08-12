tests/ui/issues/issue-25746-bool-transmute.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
use std::mem::transmute;

fn main() {
    unsafe {
        let _: i8 = transmute(false);
        let _: i8 = transmute(true);
        let _: bool = transmute(0u8);
        let _: bool = transmute(1u8);
    }
}


