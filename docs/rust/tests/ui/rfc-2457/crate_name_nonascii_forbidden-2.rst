tests/ui/rfc-2457/crate_name_nonascii_forbidden-2.rs
====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags:--extern му_сгате
// edition:2018

use му_сгате::baz; //~  ERROR cannot load a crate with a non-ascii name `му_сгате`

fn main() {}


