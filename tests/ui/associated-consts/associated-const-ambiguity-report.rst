tests/ui/associated-consts/associated-const-ambiguity-report.rs
===============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    trait Foo {
    const ID: i32;
}

trait Bar {
    const ID: i32;
}

impl Foo for i32 {
    const ID: i32 = 1;
}

impl Bar for i32 {
    const ID: i32 = 3;
}

const X: i32 = <i32>::ID; //~ ERROR E0034

fn main() {
    assert_eq!(1, X);
}


