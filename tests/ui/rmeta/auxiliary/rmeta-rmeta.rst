tests/ui/rmeta/auxiliary/rmeta-rmeta.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // no-prefer-dynamic
// compile-flags: --emit=metadata

#![crate_type="rlib"]
#![crate_name="rmeta_aux"]

pub struct Foo {
    pub field2: i32,
}


