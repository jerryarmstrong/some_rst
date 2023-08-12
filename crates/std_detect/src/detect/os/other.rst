crates/std_detect/src/detect/os/other.rs
========================================

Last edited: 2019-05-15 21:04:28

Contents:

.. code-block:: rs

    //! Other operating systems

use crate::detect::Feature;

/// Performs run-time feature detection.
#[inline]
pub fn check_for(_x: Feature) -> bool {
    false
}


