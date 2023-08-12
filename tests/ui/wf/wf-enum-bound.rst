tests/ui/wf/wf-enum-bound.rs
============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test that we check enum bounds for WFedness.

#![feature(associated_type_defaults)]

#![allow(dead_code)]

trait ExtraCopy<T:Copy> { }

enum SomeEnum<T,U>
    where T: ExtraCopy<U> //~ ERROR E0277
{
    SomeVariant(T,U)
}


fn main() { }


