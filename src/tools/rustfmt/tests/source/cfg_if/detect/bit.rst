src/tools/rustfmt/tests/source/cfg_if/detect/bit.rs
===================================================

Last edited: 2023-03-30 20:35:59

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


