compiler/rustc_index/src/lib.rs
===============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![deny(rustc::untranslatable_diagnostic)]
#![deny(rustc::diagnostic_outside_of_impl)]
#![cfg_attr(
    feature = "nightly",
    feature(
        allow_internal_unstable,
        extend_one,
        min_specialization,
        new_uninit,
        step_trait,
        stmt_expr_attributes,
        test
    )
)]

#[cfg(feature = "nightly")]
pub mod bit_set;
#[cfg(feature = "nightly")]
pub mod interval;
pub mod vec;

#[cfg(feature = "rustc_macros")]
pub use rustc_macros::newtype_index;

/// Type size assertion. The first argument is a type and the second argument is its expected size.
#[macro_export]
macro_rules! static_assert_size {
    ($ty:ty, $size:expr) => {
        const _: [(); $size] = [(); ::std::mem::size_of::<$ty>()];
    };
}


