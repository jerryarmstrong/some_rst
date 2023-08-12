tests/ui/inline-const/const-expr-basic.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

#![feature(inline_const)]

fn foo() -> i32 {
    const {
        let x = 5 + 10;
        x / 3
    }
}

fn main() {
    assert_eq!(5, foo());
}


