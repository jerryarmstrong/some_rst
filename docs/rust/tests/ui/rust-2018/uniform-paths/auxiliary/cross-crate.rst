tests/ui/rust-2018/uniform-paths/auxiliary/cross-crate.rs
=========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // edition:2018

pub use ignore as built_in_attr;
pub use u8 as built_in_type;
pub use rustfmt as tool_mod;


