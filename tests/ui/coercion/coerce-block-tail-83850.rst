tests/ui/coercion/coerce-block-tail-83850.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-fail
fn f(_: &[i32]) {}

fn main() {
    f(&Box::new([1, 2]));
    //~^ ERROR mismatched types
}


