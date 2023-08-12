tests/ui/cfg/cfg-target-abi.rs
==============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![feature(cfg_target_abi)]

#[cfg(target_abi = "eabihf")]
pub fn main() {
}

#[cfg(not(target_abi = "eabihf"))]
pub fn main() {
}


