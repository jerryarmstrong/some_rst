tests/ui/consts/const-eval/promote_mutable_zst_mir_borrowck.rs
==============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

pub fn main() {
    let y: &'static mut [u8; 0] = &mut [];
}


