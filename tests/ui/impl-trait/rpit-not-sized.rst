tests/ui/impl-trait/rpit-not-sized.rs
=====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn foo() -> impl ?Sized {
    //~^ ERROR the size for values of type `impl ?Sized` cannot be known at compilation time
    ()
}

fn main() {}


