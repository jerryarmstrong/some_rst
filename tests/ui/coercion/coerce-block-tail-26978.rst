tests/ui/coercion/coerce-block-tail-26978.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-fail
fn f(_: &i32) {}

fn main() {
    let x = Box::new(1i32);

    f(&x);
    f(&(x));
    f(&{x});
    //~^ ERROR mismatched types
}


