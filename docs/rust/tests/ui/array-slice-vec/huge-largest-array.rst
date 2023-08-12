tests/ui/array-slice-vec/huge-largest-array.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass


use std::mem::size_of;

#[cfg(target_pointer_width = "32")]
pub fn main() {
    assert_eq!(size_of::<[u8; (1 << 31) - 1]>(), (1 << 31) - 1);
}

#[cfg(target_pointer_width = "64")]
pub fn main() {
    assert_eq!(size_of::<[u8; (1 << 47) - 1]>(), (1 << 47) - 1);
}


