tests/ui/wf/wf-trait-associated-type-bound.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test that we check associated type bounds for WFedness.

#![feature(associated_type_defaults)]

#![allow(dead_code)]

trait ExtraCopy<T:Copy> { }

trait SomeTrait<T> {
    type Type1: ExtraCopy<T>; //~ ERROR E0277
}


fn main() { }


