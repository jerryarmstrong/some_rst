tests/ui/suggestions/call-boxed.rs
==================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let mut x = 1i32;
    let y = Box::new(|| 1);
    x = y;
    //~^ ERROR mismatched types
    //~| HELP use parentheses to call this closure
}


