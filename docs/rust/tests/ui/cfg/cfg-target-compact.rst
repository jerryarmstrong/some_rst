tests/ui/cfg/cfg-target-compact.rs
==================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![feature(cfg_target_compact)]

#[cfg(target(os = "linux", pointer_width = "64"))]
pub fn main() {
}

#[cfg(not(target(os = "linux", pointer_width = "64")))]
pub fn main() {
}


