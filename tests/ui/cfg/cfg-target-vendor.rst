tests/ui/cfg/cfg-target-vendor.rs
=================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#[cfg(target_vendor = "unknown")]
pub fn main() {
}

#[cfg(not(target_vendor = "unknown"))]
pub fn main() {
}


