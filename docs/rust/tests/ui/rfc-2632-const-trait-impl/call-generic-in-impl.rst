tests/ui/rfc-2632-const-trait-impl/call-generic-in-impl.rs
==========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
#![feature(const_trait_impl)]

#[const_trait]
trait MyPartialEq {
    fn eq(&self, other: &Self) -> bool;
}

impl<T: ~const PartialEq> const MyPartialEq for T {
    fn eq(&self, other: &Self) -> bool {
        PartialEq::eq(self, other)
    }
}

fn main() {}


