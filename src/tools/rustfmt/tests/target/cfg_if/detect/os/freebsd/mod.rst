src/tools/rustfmt/tests/target/cfg_if/detect/os/freebsd/mod.rs
==============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    //! Run-time feature detection on FreeBSD

mod auxvec;

cfg_if! {
    if #[cfg(target_arch = "aarch64")] {
        mod aarch64;
        pub use self::aarch64::check_for;
    } else if #[cfg(target_arch = "arm")] {
        mod arm;
        pub use self::arm::check_for;
    } else if #[cfg(target_arch = "powerpc64")] {
        mod powerpc;
        pub use self::powerpc::check_for;
    } else {
        use crate::arch::detect::Feature;
        /// Performs run-time feature detection.
        pub fn check_for(_x: Feature) -> bool {
            false
        }
    }
}


