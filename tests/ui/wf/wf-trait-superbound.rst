tests/ui/wf/wf-trait-superbound.rs
==================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test that we check supertrait bounds for WFedness.

#![feature(associated_type_defaults)]
#![feature(rustc_attrs)]
#![allow(dead_code)]

trait ExtraCopy<T:Copy> { }

trait SomeTrait<T>: ExtraCopy<T> { //~ ERROR E0277
}

fn main() { }


