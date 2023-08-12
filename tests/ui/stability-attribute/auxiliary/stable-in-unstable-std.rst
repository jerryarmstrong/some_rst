tests/ui/stability-attribute/auxiliary/stable-in-unstable-std.rs
================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(staged_api)]
#![feature(unstable_test_feature)]
#![stable(feature = "stable_test_feature", since = "1.2.0")]

extern crate stable_in_unstable_core;

#[stable(feature = "stable_test_feature", since = "1.2.0")]
pub mod old_stable_module {
    #[stable(feature = "stable_test_feature", since = "1.2.0")]
    pub use stable_in_unstable_core::new_unstable_module::OldTrait;
}


