tests/ui/rfc-2457/mod_file_nonascii_with_path_allowed.rs
========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

#[path="auxiliary/mod_file_nonascii_with_path_allowed-aux.rs"]
mod řųśť;

fn main() {}


