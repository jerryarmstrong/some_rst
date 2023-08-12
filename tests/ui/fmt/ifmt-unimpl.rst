tests/ui/fmt/ifmt-unimpl.rs
===========================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    format!("{:X}", "3");
    //~^ ERROR: `str: UpperHex` is not satisfied
}


