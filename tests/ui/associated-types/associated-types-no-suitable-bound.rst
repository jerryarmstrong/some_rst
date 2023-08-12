tests/ui/associated-types/associated-types-no-suitable-bound.rs
===============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    trait Get {
    type Value;
    fn get(&self) -> <Self as Get>::Value;
}

struct Struct {
    x: isize,
}

impl Struct {
    fn uhoh<T>(foo: <T as Get>::Value) {}
    //~^ ERROR the trait bound `T: Get` is not satisfied
}

fn main() {
}


