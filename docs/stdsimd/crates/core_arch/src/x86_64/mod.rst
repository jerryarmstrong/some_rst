crates/core_arch/src/x86_64/mod.rs
==================================

Last edited: 2019-05-15 21:04:28

Contents:

.. code-block:: rs

    //! `x86_64` intrinsics

mod fxsr;
pub use self::fxsr::*;

mod sse;
pub use self::sse::*;

mod sse2;
pub use self::sse2::*;

mod sse41;
pub use self::sse41::*;

mod sse42;
pub use self::sse42::*;

mod xsave;
pub use self::xsave::*;

mod abm;
pub use self::abm::*;

mod avx;
pub use self::avx::*;

mod bmi;
pub use self::bmi::*;

mod bmi2;
pub use self::bmi2::*;

mod avx2;
pub use self::avx2::*;

mod bswap;
pub use self::bswap::*;

mod rdrand;
pub use self::rdrand::*;

mod cmpxchg16b;
pub use self::cmpxchg16b::*;

mod adx;
pub use self::adx::*;

mod bt;
pub use self::bt::*;


