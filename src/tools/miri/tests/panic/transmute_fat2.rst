src/tools/miri/tests/panic/transmute_fat2.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    #[cfg(all(target_endian = "little", target_pointer_width = "64"))]
    let bad = unsafe { std::mem::transmute::<u128, &[u8]>(42) };
    #[cfg(all(target_endian = "big", target_pointer_width = "64"))]
    let bad = unsafe { std::mem::transmute::<u128, &[u8]>(42 << 64) };
    #[cfg(all(target_endian = "little", target_pointer_width = "32"))]
    let bad = unsafe { std::mem::transmute::<u64, &[u8]>(42) };
    // This created a slice with length 0, so the following will fail the bounds check.
    bad[0];
}


