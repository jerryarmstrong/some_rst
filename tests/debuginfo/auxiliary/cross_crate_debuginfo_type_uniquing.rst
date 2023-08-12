tests/debuginfo/auxiliary/cross_crate_debuginfo_type_uniquing.rs
================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // no-prefer-dynamic
#![crate_type = "rlib"]
// compile-flags:-g

struct S1;

impl S1 {
    fn f(&mut self) { }
}


struct S2;

impl S2 {
    fn f(&mut self) { }
}


