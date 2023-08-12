tests/ui/rfc-2632-const-trait-impl/default-method-body-is-const-same-trait-ck.rs
================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(const_trait_impl)]

#[const_trait]
pub trait Tr {
    fn a(&self) {}

    fn b(&self) {
        ().a()
        //~^ ERROR the trait bound
    }
}

impl Tr for () {}

fn main() {}


