tests/ui/wasm/simd-to-array-80108.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // only-wasm32
// compile-flags: --crate-type=lib -Copt-level=2
// build-pass
#![feature(repr_simd)]

// Regression test for #80108

#[repr(simd)]
pub struct Vector([i32; 4]);

impl Vector {
    pub const fn to_array(self) -> [i32; 4] {
        self.0
    }
}


