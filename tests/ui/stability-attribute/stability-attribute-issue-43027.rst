tests/ui/stability-attribute/stability-attribute-issue-43027.rs
===============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
#![feature(staged_api)]
#![stable(feature = "test", since = "0")]

#[stable(feature = "test", since = "0")]
pub struct A<T>(pub T);

#[stable(feature = "test", since = "0")]
pub struct B<T>(#[stable(feature = "test", since = "0")] pub T);

fn main() {
    // Make sure the field is used to fill the stability cache
    A(0).0;
    B(0).0;
}


