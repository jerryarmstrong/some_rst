tests/ui/consts/int_ptr_for_zst_slices.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

const FOO: &str = unsafe { &*(1_usize as *const [u8; 0] as *const [u8] as *const str) };

fn main() {}


