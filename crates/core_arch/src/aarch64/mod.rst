crates/core_arch/src/aarch64/mod.rs
===================================

Last edited: 2019-05-15 21:04:28

Contents:

.. code-block:: rs

    //! AArch64 intrinsics.
//!
//! The reference for NEON is [ARM's NEON Intrinsics Reference][arm_ref]. The
//! [ARM's NEON Intrinsics Online Database][arm_dat] is also useful.
//!
//! [arm_ref]: http://infocenter.arm.com/help/topic/com.arm.doc.ihi0073a/IHI0073A_arm_neon_intrinsics_ref.pdf
//! [arm_dat]: https://developer.arm.com/technologies/neon/intrinsics

mod v8;
pub use self::v8::*;

mod neon;
pub use self::neon::*;

mod crypto;
pub use self::crypto::*;

mod crc;
pub use self::crc::*;

pub use super::acle::*;

#[cfg(test)]
use stdsimd_test::assert_instr;

/// Generates the trap instruction `BRK 1`
#[cfg_attr(test, assert_instr(brk))]
#[inline]
pub unsafe fn brk() -> ! {
    crate::intrinsics::abort()
}


