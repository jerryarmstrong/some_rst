crates/core_arch/src/powerpc/mod.rs
===================================

Last edited: 2019-05-15 21:04:28

Contents:

.. code-block:: rs

    //! PowerPC intrinsics

#[cfg(target_feature = "altivec")]
mod altivec;
#[cfg(target_feature = "altivec")]
pub use self::altivec::*;

mod vsx;
pub use self::vsx::*;

#[cfg(test)]
use stdsimd_test::assert_instr;

/// Generates the trap instruction `TRAP`
#[cfg_attr(test, assert_instr(trap))]
#[inline]
pub unsafe fn trap() -> ! {
    crate::intrinsics::abort()
}


