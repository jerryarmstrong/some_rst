tests/ui/parser/trailing-question-in-type.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-rustfix

fn foo() -> i32? { //~ ERROR invalid `?` in type
    let x: i32? = Some(1); //~ ERROR invalid `?` in type
    x
}

fn main() {
    let _: Option<i32> = foo();
}


