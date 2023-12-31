src/tools/rustfmt/tests/target/cfg_if/detect/arch/mips64.rs
===========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    //! Run-time feature detection on MIPS64.

/// Checks if `mips64` feature is enabled.
#[macro_export]
#[unstable(feature = "stdsimd", issue = "27731")]
#[allow_internal_unstable(stdsimd_internal, stdsimd)]
macro_rules! is_mips64_feature_detected {
    ("msa") => {
        cfg!(target_feature = "msa") || $crate::detect::check_for($crate::detect::Feature::msa)
    };
    ($t:tt,) => {
        is_mips64_feature_detected!($t);
    };
    ($t:tt) => {
        compile_error!(concat!("unknown mips64 target feature: ", $t))
    };
}

/// MIPS64 CPU Feature enum. Each variant denotes a position in a bitset
/// for a particular feature.
///
/// PLEASE: do not use this, it is an implementation detail subject to change.
#[doc(hidden)]
#[allow(non_camel_case_types)]
#[repr(u8)]
#[unstable(feature = "stdsimd_internal", issue = "0")]
pub enum Feature {
    /// MIPS SIMD Architecture (MSA)
    msa,
}


