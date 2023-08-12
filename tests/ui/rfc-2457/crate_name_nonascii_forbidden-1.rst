tests/ui/rfc-2457/crate_name_nonascii_forbidden-1.rs
====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    extern crate ьаг; //~ ERROR cannot load a crate with a non-ascii name `ьаг`

fn main() {}


