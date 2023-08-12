tests/ui/wf/wf-trait-associated-type-trait.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test that we check associated type default values for WFedness.

#![feature(associated_type_defaults)]

#![allow(dead_code)]

struct IsCopy<T:Copy> { x: T }

trait SomeTrait {
    type Type1;
    type Type2 = (IsCopy<Self::Type1>, bool);
    //~^ ERROR E0277
}


fn main() { }


