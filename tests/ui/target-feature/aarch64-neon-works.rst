tests/ui/target-feature/aarch64-neon-works.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // only-aarch64
// run-pass
#![allow(dead_code)]
use std::arch::*;
use std::arch::aarch64::*;

// Smoke test to verify aarch64 code that enables NEON compiles.
fn main() {
    let _zero = if is_aarch64_feature_detected!("neon") {
        unsafe {
            let zeros = zero_vector();
            vgetq_lane_u8::<1>(zeros)
        }
    } else {
        0
    };
}


#[target_feature(enable = "neon")]
unsafe fn zero_vector() -> uint8x16_t {
    vmovq_n_u8(0)
}


