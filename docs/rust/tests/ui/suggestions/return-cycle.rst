tests/ui/suggestions/return-cycle.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use std::marker::PhantomData;

struct Token<T>(PhantomData<T>);

impl<T> Token<T> {
    fn new() -> _ {
        //~^ ERROR the placeholder `_` is not allowed within types on item signatures for return types
        //~| NOTE not allowed in type signatures
        //~| HELP replace with the correct return type
        Token(PhantomData::<()>)
    }
}

fn main() {}


