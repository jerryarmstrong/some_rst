tests/ui/parser/inner-attr-in-trait-def.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

#![deny(non_camel_case_types)]

fn main() {}

trait foo_bar {
    #![allow(non_camel_case_types)]
}


