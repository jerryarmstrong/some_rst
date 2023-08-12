tests/ui/fmt/ifmt-unknown-trait.rs
==================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    format!("{:notimplemented}", "3");
    //~^ ERROR: unknown format trait `notimplemented`
}


