tests/ui/privacy/auxiliary/privacy_reexport.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    pub extern crate core;
pub use foo as bar;

pub mod foo {
    pub fn frob() {}
}


