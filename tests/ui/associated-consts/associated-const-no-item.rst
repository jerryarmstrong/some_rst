tests/ui/associated-consts/associated-const-no-item.rs
======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    trait Foo {
    const ID: i32;
}

const X: i32 = <i32>::ID;
//~^ ERROR no associated item named `ID` found

fn main() {
    assert_eq!(1, X);
}


