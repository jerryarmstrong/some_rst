tests/rustdoc-ui/doc_cfg_hide.rs
================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(doc_cfg_hide)]
#![deny(warnings)]

#![doc(cfg_hide = "test")] //~ ERROR
//~^ WARN
#![doc(cfg_hide)] //~ ERROR
//~^ WARN

#[doc(cfg_hide(doc))] //~ ERROR
//~^ WARN
pub fn foo() {}


