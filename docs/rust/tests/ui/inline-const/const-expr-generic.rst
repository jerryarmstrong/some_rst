tests/ui/inline-const/const-expr-generic.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
#![feature(inline_const)]

fn foo<T>() -> usize {
    const { std::mem::size_of::<T>() }
}

fn bar<const N: usize>() -> usize {
    const { N + 1 }
}

fn main() {
    foo::<i32>();
    bar::<1>();
}


