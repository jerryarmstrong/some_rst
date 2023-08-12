tests/ui/rfc-2457/mod_file_nonascii_forbidden.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    mod řųśť; //~ trying to load file for
//~^ file not found for

fn main() {}


