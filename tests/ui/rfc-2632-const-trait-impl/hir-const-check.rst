tests/ui/rfc-2632-const-trait-impl/hir-const-check.rs
=====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Regression test for #69615.

#![feature(const_trait_impl)]

#[const_trait]
pub trait MyTrait {
    fn method(&self) -> Option<()>;
}

impl const MyTrait for () {
    fn method(&self) -> Option<()> {
        Some(())?; //~ ERROR `?` is not allowed in a `const fn`
        None
    }
}

fn main() {}


