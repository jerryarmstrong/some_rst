tests/codegen-units/item-collection/unreferenced-const-fn.rs
============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags:-Zprint-mono-items=lazy

#![deny(dead_code)]
#![crate_type = "rlib"]

//~ MONO_ITEM fn foo @@ unreferenced_const_fn-cgu.0[External]
pub const fn foo(x: u32) -> u32 {
    x + 0xf00
}


