tests/ui/unresolved/unresolved-asterisk-imports.rs
==================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use not_existing_crate::*; //~ ERROR unresolved import `not_existing_crate
use std as foo;

fn main() {}


