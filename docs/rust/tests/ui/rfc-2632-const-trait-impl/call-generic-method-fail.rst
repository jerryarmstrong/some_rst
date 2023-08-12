tests/ui/rfc-2632-const-trait-impl/call-generic-method-fail.rs
==============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(const_trait_impl)]

pub const fn equals_self<T: PartialEq>(t: &T) -> bool {
    *t == *t
    //~^ ERROR can't compare
}

fn main() {}


