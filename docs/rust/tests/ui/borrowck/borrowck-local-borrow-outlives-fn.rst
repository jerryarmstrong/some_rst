tests/ui/borrowck/borrowck-local-borrow-outlives-fn.rs
======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn cplusplus_mode(x: isize) -> &'static isize {
    &x
    //~^ ERROR cannot return reference to function parameter `x` [E0515]
}

fn main() {}


