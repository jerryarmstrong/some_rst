tests/ui/type/type-annotation-needed.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn foo<T: Into<String>>(x: i32) {}
//~^ NOTE required by
//~| NOTE required by

fn main() {
    foo(42);
    //~^ ERROR type annotations needed
    //~| NOTE cannot infer type
    //~| NOTE cannot satisfy
}


