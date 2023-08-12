tests/ui/linkage-attr/auxiliary/def_external.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(linkage)]
#![crate_type = "lib"]

#[linkage="external"]
pub static EXTERN: u32 = 0;


