tests/rustdoc-gui/src/staged_api/lib.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(staged_api)]
#![stable(feature = "some_feature", since = "1.3.5")]

#[stable(feature = "some_feature", since = "1.3.5")]
pub struct Foo {}

impl Foo {
    #[stable(feature = "some_feature", since = "1.3.5")]
    pub fn bar() {}
    #[stable(feature = "some_other_feature", since = "1.3.6")]
    pub fn yo() {}
}


