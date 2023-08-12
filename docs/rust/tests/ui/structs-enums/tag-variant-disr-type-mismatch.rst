tests/ui/structs-enums/tag-variant-disr-type-mismatch.rs
========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(dead_code)]
#![allow(non_camel_case_types)]

// pretty-expanded FIXME #23616

enum color {
    red = 1,
    blue = 2,
}

pub fn main() {}


