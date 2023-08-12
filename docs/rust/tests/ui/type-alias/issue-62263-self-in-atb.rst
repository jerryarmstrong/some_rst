tests/ui/type-alias/issue-62263-self-in-atb.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    pub trait Trait {
    type A;
}

pub type Alias = dyn Trait<A = Self::A>;
//~^ ERROR failed to resolve: `Self`

fn main() {}


