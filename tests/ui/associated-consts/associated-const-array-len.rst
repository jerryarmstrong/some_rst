tests/ui/associated-consts/associated-const-array-len.rs
========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    trait Foo {
    const ID: usize;
}

const X: [i32; <i32 as Foo>::ID] = [0, 1, 2];
//~^ ERROR the trait bound `i32: Foo` is not satisfied

fn main() {
    assert_eq!(1, X);
}


