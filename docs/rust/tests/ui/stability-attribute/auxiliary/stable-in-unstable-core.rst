tests/ui/stability-attribute/auxiliary/stable-in-unstable-core.rs
=================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(staged_api)]
#![stable(feature = "stable_test_feature", since = "1.2.0")]

#[unstable(feature = "unstable_test_feature", issue = "1")]
pub mod new_unstable_module {
    #[stable(feature = "stable_test_feature", since = "1.2.0")]
    pub trait OldTrait {}
}


