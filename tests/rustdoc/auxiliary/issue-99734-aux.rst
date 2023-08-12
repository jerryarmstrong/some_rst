tests/rustdoc/auxiliary/issue-99734-aux.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    pub struct Option;
impl Option {
    pub fn unwrap(self) {}
}

/// [`Option::unwrap`]
pub mod task {}

extern "C" {
    pub fn main() -> std::ffi::c_int;
}


