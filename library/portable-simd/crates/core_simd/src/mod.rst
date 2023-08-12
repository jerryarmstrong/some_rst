library/portable-simd/crates/core_simd/src/mod.rs
=================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[macro_use]
mod swizzle;

pub(crate) mod intrinsics;

#[cfg(feature = "generic_const_exprs")]
mod to_bytes;

mod elements;
mod eq;
mod fmt;
mod iter;
mod lane_count;
mod masks;
mod ops;
mod ord;
mod select;
mod vector;
mod vendor;

#[doc = include_str!("core_simd_docs.md")]
pub mod simd {
    pub(crate) use crate::core_simd::intrinsics;

    pub use crate::core_simd::elements::*;
    pub use crate::core_simd::eq::*;
    pub use crate::core_simd::lane_count::{LaneCount, SupportedLaneCount};
    pub use crate::core_simd::masks::*;
    pub use crate::core_simd::ord::*;
    pub use crate::core_simd::swizzle::*;
    pub use crate::core_simd::vector::*;
}


