library/portable-simd/crates/core_simd/src/lib.rs
=================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![no_std]
#![feature(
    convert_float_to_int,
    decl_macro,
    intra_doc_pointers,
    platform_intrinsics,
    repr_simd,
    simd_ffi,
    staged_api,
    stdsimd
)]
#![cfg_attr(feature = "generic_const_exprs", feature(generic_const_exprs))]
#![cfg_attr(feature = "generic_const_exprs", allow(incomplete_features))]
#![warn(missing_docs)]
#![deny(unsafe_op_in_unsafe_fn, clippy::undocumented_unsafe_blocks)]
#![unstable(feature = "portable_simd", issue = "86656")]
//! Portable SIMD module.

#[path = "mod.rs"]
mod core_simd;
pub use self::core_simd::simd;
pub use simd::*;


