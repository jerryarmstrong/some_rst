tests/ui/feature-gates/feature-gate-simd-ffi.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(repr_simd)]
#![allow(dead_code)]

#[repr(simd)]
#[derive(Copy, Clone)]
struct LocalSimd(u8, u8);

extern "C" {
    fn baz() -> LocalSimd; //~ ERROR use of SIMD type
    fn qux(x: LocalSimd); //~ ERROR use of SIMD type
}

fn main() {}


