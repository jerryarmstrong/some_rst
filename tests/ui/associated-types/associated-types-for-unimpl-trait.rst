tests/ui/associated-types/associated-types-for-unimpl-trait.rs
==============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-rustfix
#![allow(unused_variables)]

trait Get {
    type Value;
    fn get(&self) -> <Self as Get>::Value;
}

trait Other {
    fn uhoh<U:Get>(&self, foo: U, bar: <Self as Get>::Value) {}
    //~^ ERROR the trait bound `Self: Get` is not satisfied
}

fn main() {
}


