tests/ui/borrowck/move-error-in-promoted-2.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Regression test for #70934

struct S;

fn foo() {
    &([S][0],);
    //~^ ERROR cannot move out of type `[S; 1]`
}

fn main() {}


