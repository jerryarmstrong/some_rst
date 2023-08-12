tests/ui/use/use-meta-mismatch.rs
=================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // error-pattern:can't find crate for `fake_crate`

extern crate fake_crate as extra;

fn main() { }


