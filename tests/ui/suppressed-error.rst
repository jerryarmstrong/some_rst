tests/ui/suppressed-error.rs
============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let (x, y) = ();
//~^ ERROR mismatched types
//~| expected unit type `()`
//~| found tuple `(_, _)`
//~| expected `()`, found tuple
    return x;
}


