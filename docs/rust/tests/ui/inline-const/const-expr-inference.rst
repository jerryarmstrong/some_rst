tests/ui/inline-const/const-expr-inference.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

#![feature(inline_const)]

pub fn todo<T>() -> T {
    const { todo!() }
}

fn main() {
    let _: usize = const { 0 };
}


