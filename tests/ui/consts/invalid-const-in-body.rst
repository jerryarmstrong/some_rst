tests/ui/consts/invalid-const-in-body.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn f() -> impl Sized {
    2.0E
    //~^ ERROR expected at least one digit in exponent
}

fn main() {}


