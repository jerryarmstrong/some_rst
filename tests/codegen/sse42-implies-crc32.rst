tests/codegen/sse42-implies-crc32.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // only-x86_64
// min-llvm-version: 14.0
// compile-flags: -Copt-level=3

#![crate_type = "lib"]

#[cfg(target_arch = "x86_64")]
#[target_feature(enable = "sse4.2")]
#[no_mangle]
pub unsafe fn crc32sse(v: u8) -> u32 {
    use std::arch::x86_64::*;
    let out = !0u32;
    _mm_crc32_u8(out, v)
}

// CHECK: attributes #0 {{.*"target-features"="\+sse4.2,\+crc32"}}


