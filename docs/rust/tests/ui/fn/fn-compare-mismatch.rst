tests/ui/fn/fn-compare-mismatch.rs
==================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    fn f() { }
    fn g() { }
    let x = f == g;
    //~^ ERROR binary operation `==` cannot be applied
    //~| ERROR mismatched types
}


