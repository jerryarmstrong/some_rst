tests/ui/pattern/usefulness/auxiliary/unstable.rs
=================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(staged_api)]
#![stable(feature = "stable_test_feature", since = "1.0.0")]

#[stable(feature = "stable_test_feature", since = "1.0.0")]
pub enum UnstableEnum {
    #[stable(feature = "stable_test_feature", since = "1.0.0")]
    Stable,
    #[stable(feature = "stable_test_feature", since = "1.0.0")]
    Stable2,
    #[unstable(feature = "unstable_test_feature", issue = "none")]
    Unstable,
}

#[derive(Default)]
#[stable(feature = "stable_test_feature", since = "1.0.0")]
pub struct UnstableStruct {
    #[stable(feature = "stable_test_feature", since = "1.0.0")]
    pub stable: bool,
    #[stable(feature = "stable_test_feature", since = "1.0.0")]
    pub stable2: usize,
    #[unstable(feature = "unstable_test_feature", issue = "none")]
    pub unstable: u8,
}


