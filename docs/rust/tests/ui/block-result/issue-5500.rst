tests/ui/block-result/issue-5500.rs
===================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    &panic!()
    //~^ ERROR mismatched types
    //~| expected unit type `()`
    //~| found reference `&_`
    //~| expected `()`, found reference
}


