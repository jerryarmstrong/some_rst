tests/ui/rfc-2126-crate-paths/keyword-crate-as-identifier.rs
============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let crate = 0;
    //~^ ERROR expected unit struct, unit variant or constant, found module `crate`
}


