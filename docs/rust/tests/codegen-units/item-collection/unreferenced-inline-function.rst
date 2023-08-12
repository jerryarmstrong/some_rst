tests/codegen-units/item-collection/unreferenced-inline-function.rs
===================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags:-Zprint-mono-items=lazy

// N.B., we do not expect *any* monomorphization to be generated here.

#![deny(dead_code)]
#![crate_type = "rlib"]

#[inline]
pub fn foo() -> bool {
    [1, 2] == [3, 4]
}


