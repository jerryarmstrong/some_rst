src/tools/rustfmt/tests/target/cfg_if/detect/os/other.rs
========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    //! Other operating systems

use crate::detect::Feature;

/// Performs run-time feature detection.
#[inline]
pub fn check_for(_x: Feature) -> bool {
    false
}


