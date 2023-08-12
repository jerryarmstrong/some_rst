tests/ui/unsized-locals/issue-50940-with-feature.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(unsized_locals, unsized_fn_params)]
//~^ WARN the feature `unsized_locals` is incomplete

fn main() {
    struct A<X: ?Sized>(X);
    A as fn(str) -> A<str>;
    //~^ERROR the size for values of type `str` cannot be known at compilation time
}


