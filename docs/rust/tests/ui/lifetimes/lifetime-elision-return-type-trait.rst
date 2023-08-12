tests/ui/lifetimes/lifetime-elision-return-type-trait.rs
========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    trait Future {
    type Item;
    type Error;
}

use std::error::Error;

fn foo() -> impl Future<Item=(), Error=Box<dyn Error>> {
    //~^ ERROR not satisfied
    Ok(())
}

fn main() {}


