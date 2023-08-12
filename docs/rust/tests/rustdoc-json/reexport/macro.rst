tests/rustdoc-json/reexport/macro.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // edition:2018

#![no_core]
#![feature(no_core)]

// @set repro_id = "$.index[*][?(@.name=='repro')].id"
#[macro_export]
macro_rules! repro {
    () => {};
}

// @set repro2_id = "$.index[*][?(@.inner.name=='repro2')].id"
pub use crate::repro as repro2;

// @ismany "$.index[*][?(@.name=='macro')].inner.items[*]" $repro_id $repro2_id


