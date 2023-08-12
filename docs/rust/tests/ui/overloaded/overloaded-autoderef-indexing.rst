tests/ui/overloaded/overloaded-autoderef-indexing.rs
====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

use std::ops::Deref;

struct DerefArray<'a, T:'a> {
    inner: &'a [T]
}

impl<'a, T> Deref for DerefArray<'a, T> {
    type Target = &'a [T];

    fn deref<'b>(&'b self) -> &'b &'a [T] {
        &self.inner
    }
}

pub fn main() {
    let a = &[1, 2, 3];
    assert_eq!(DerefArray {inner: a}[1], 2);
}


