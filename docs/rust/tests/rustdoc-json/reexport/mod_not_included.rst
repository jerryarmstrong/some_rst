tests/rustdoc-json/reexport/mod_not_included.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Regression test for https://github.com/rust-lang/rust/issues/101103

#![feature(no_core)]
#![no_core]

mod m1 {
    pub fn x() {}
}

pub use m1::x;

// @has "$.index[*][?(@.name=='x' && @.kind=='function')]"
// @has "$.index[*][?(@.kind=='import' && @.inner.name=='x')].inner.source" '"m1::x"'
// @!has "$.index[*][?(@.name=='m1')]"


