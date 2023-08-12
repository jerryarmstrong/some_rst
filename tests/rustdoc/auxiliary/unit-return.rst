tests/rustdoc/auxiliary/unit-return.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    pub fn f2<F: FnMut(u32) + Clone>(f: F) {}

pub fn f3<F: FnMut(u64) -> () + Clone>(f: F) {}


