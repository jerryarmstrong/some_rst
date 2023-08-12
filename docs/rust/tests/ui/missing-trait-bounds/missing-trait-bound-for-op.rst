tests/ui/missing-trait-bounds/missing-trait-bound-for-op.rs
===========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-rustfix

pub fn foo<T>(s: &[T], t: &[T]) {
    let _ = s == t; //~ ERROR binary operation `==` cannot be applied to type `&[T]`
}

fn main() {}


