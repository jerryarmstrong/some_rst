tests/ui/single-use-lifetime/derive-eq.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

#![deny(single_use_lifetimes)]

#[derive(PartialEq, Eq)]
struct Foo<'a, T> {
    /// a reference to the underlying secret data that will be derefed
    pub data: &'a mut T,
}

fn main() {}


