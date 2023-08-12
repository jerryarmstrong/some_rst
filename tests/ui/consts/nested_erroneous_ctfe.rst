tests/ui/consts/nested_erroneous_ctfe.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    [9; || [9; []]];
    //~^ ERROR: mismatched types
}


