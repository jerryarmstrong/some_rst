tests/ui/wf/wf-enum-fields.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test that we check struct fields for WFedness.

#![feature(associated_type_defaults)]

#![allow(dead_code)]

struct IsCopy<T:Copy> {
    value: T
}

enum SomeEnum<A> {
    SomeVariant(IsCopy<A>) //~ ERROR E0277
}


fn main() { }


