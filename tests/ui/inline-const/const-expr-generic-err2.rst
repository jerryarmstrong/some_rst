tests/ui/inline-const/const-expr-generic-err2.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(inline_const)]

fn foo<T>() {
    let _ = [0u8; const { std::mem::size_of::<T>() }];
    //~^ ERROR: constant expression depends on a generic parameter
}

fn main() {
    foo::<i32>();
}


