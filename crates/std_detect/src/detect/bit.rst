crates/std_detect/src/detect/bit.rs
===================================

Last edited: 2019-05-15 21:04:28

Contents:

.. code-block:: rs

    //! Bit manipulation utilities.

/// Tests the `bit` of `x`.
#[allow(dead_code)]
#[inline]
pub(crate) fn test(x: usize, bit: u32) -> bool {
    debug_assert!(bit < 32, "bit index out-of-bounds");
    x & (1 << bit) != 0
}


