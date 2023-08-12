tests/ui/suggestions/dont-suggest-ufcs-for-const.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    1_u32.MAX();
    //~^ ERROR no method named `MAX` found for type `u32` in the current scope
}


