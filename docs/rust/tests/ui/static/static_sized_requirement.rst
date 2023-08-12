tests/ui/static/static_sized_requirement.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // build-pass (FIXME(62277): could be check-pass?)

#![feature(no_core, lang_items)]
#![no_core]
#![crate_type = "lib"]

#[lang = "sized"]
trait Sized {}

extern "C" {
    pub static A: u32;
}


