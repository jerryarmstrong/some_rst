tests/ui/inline-const/const-expr-generic-err.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // build-fail
#![feature(inline_const)]

fn foo<T>() {
    const { assert!(std::mem::size_of::<T>() == 0); } //~ ERROR E0080
}

fn bar<const N: usize>() -> usize {
    const { N - 1 } //~ ERROR E0080
}

fn main() {
    foo::<i32>();
    bar::<0>();
}


