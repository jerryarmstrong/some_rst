tests/ui/suggestions/type-ascription-instead-of-path.rs
=======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    std:io::stdin();
    //~^ ERROR failed to resolve: use of undeclared crate or module `io`
    //~| ERROR expected value, found crate
}


