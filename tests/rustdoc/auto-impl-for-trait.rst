tests/rustdoc/auto-impl-for-trait.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test for https://github.com/rust-lang/rust/issues/48463 issue.

use std::any::Any;
use std::ops::Deref;

pub struct AnyValue {
    val: Box<Any>,
}

impl Deref for AnyValue {
    type Target = Any;

    fn deref(&self) -> &Any {
        &*self.val
    }
}


