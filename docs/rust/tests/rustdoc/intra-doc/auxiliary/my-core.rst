tests/rustdoc/intra-doc/auxiliary/my-core.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(no_core, lang_items, rustdoc_internals, rustc_attrs)]
#![no_core]
#![rustc_coherence_is_core]
#![crate_type="rlib"]

#[doc(primitive = "char")]
/// Some char docs
mod char {}

impl char {
    pub fn len_utf8(self) -> usize {
        42
    }
}

#[lang = "sized"]
pub trait Sized {}

#[lang = "clone"]
pub trait Clone: Sized {}

#[lang = "copy"]
pub trait Copy: Clone {}


