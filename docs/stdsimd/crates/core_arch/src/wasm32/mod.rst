crates/core_arch/src/wasm32/mod.rs
==================================

Last edited: 2019-05-15 21:04:28

Contents:

.. code-block:: rs

    //! WASM32 intrinsics

#[cfg(test)]
use stdsimd_test::assert_instr;
#[cfg(test)]
use wasm_bindgen_test::wasm_bindgen_test;

#[cfg(any(target_feature = "atomics", dox))]
mod atomic;
#[cfg(any(target_feature = "atomics", dox))]
pub use self::atomic::*;

#[cfg(any(target_feature = "simd128", dox))]
mod simd128;
#[cfg(any(target_feature = "simd128", dox))]
pub use self::simd128::*;

mod memory;
pub use self::memory::*;

/// Generates the trap instruction `UNREACHABLE`
#[cfg_attr(test, assert_instr(unreachable))]
#[inline]
pub unsafe fn unreachable() -> ! {
    crate::intrinsics::abort()
}


