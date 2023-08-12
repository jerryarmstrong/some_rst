tests/ui/associated-types/auxiliary/associated-types-cc-lib.rs
==============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Helper for test issue-18048, which tests associated types in a
// cross-crate scenario.

#![crate_type="lib"]

pub trait Bar: Sized {
    type T;

    fn get(x: Option<Self>) -> <Self as Bar>::T;
}

impl Bar for isize {
    type T = usize;

    fn get(_: Option<isize>) -> usize { 22 }
}


