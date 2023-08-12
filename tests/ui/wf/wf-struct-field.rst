tests/ui/wf/wf-struct-field.rs
==============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test that we check struct fields for WFedness.

#![feature(associated_type_defaults)]

#![allow(dead_code)]

struct IsCopy<T:Copy> {
    value: T
}

struct SomeStruct<A> {
    data: IsCopy<A> //~ ERROR E0277
}


fn main() { }


