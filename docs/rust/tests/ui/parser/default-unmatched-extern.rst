tests/ui/parser/default-unmatched-extern.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {}

extern "C" {
    default!(); //~ ERROR cannot find macro `default` in this scope
    default do
    //~^ ERROR `default` is not followed by an item
    //~| ERROR non-item in item list
}


