tests/ui/functions-closures/fn-help-with-err-generic-is-not-function.rs
=======================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct Struct<T>(T);
impl Struct<T>
//~^ ERROR cannot find type `T` in this scope
//~| NOTE not found in this scope
//~| HELP you might be missing a type parameter
where
    T: Copy,
    //~^ ERROR cannot find type `T` in this scope
    //~| NOTE not found in this scope
{
    fn method(v: Vec<u8>) { v.len(); }
}

fn main() {}


