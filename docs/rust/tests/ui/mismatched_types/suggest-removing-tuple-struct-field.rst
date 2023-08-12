tests/ui/mismatched_types/suggest-removing-tuple-struct-field.rs
================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-rustfix

macro_rules! my_wrapper {
    ($expr:expr) => { MyWrapper($expr) }
}

pub struct MyWrapper(u32);

fn main() {
    let value = MyWrapper(123);
    some_fn(value.0); //~ ERROR mismatched types
    some_fn(my_wrapper!(123).0); //~ ERROR mismatched types
}

fn some_fn(wrapped: MyWrapper) {
    drop(wrapped);
}


