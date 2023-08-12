tests/ui/unsized/unsized-bare-typaram.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn bar<T: Sized>() { }
fn foo<T: ?Sized>() { bar::<T>() }
//~^ ERROR the size for values of type
fn main() { }


