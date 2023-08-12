tests/ui/inline-const/const-expr-reference.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

#![feature(inline_const)]

const fn bar() -> i32 {
    const {
        2 + 3
    }
}

fn main() {
    let x: &'static i32 = &const{bar()};
    assert_eq!(&5, x);
}


