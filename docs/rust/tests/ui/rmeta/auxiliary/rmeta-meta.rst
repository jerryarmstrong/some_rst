tests/ui/rmeta/auxiliary/rmeta-meta.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // no-prefer-dynamic
// compile-flags: --emit=metadata

#![crate_type="rlib"]

pub struct Foo {
    pub field: i32,
}


