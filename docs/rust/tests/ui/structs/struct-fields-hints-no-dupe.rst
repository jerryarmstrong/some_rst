tests/ui/structs/struct-fields-hints-no-dupe.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct A {
    foo : i32,
    car : i32,
    barr : i32
}

fn main() {
    let a = A {
        foo : 5,
        bar : 42,
        //~^ ERROR struct `A` has no field named `bar`
        car : 9,
    };
}


