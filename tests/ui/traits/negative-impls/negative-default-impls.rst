tests/ui/traits/negative-impls/negative-default-impls.rs
========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(negative_impls)]
#![feature(specialization)]
//~^ WARN the feature `specialization` is incomplete

trait MyTrait {
    type Foo;
}

default impl !MyTrait for u32 {} //~ ERROR negative impls cannot be default impls

fn main() {}


