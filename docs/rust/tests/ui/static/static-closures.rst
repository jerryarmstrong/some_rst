tests/ui/static/static-closures.rs
==================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    static || {};
    //~^ ERROR closures cannot be static
}


