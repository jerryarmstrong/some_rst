tests/ui/unsized/unsized-fn-arg.rs
==================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-rustfix
#![crate_type="lib"]
#![allow(unused)]

fn f<T: ?Sized>(t: T) {}
//~^ ERROR the size for values of type `T` cannot be known at compilation time


