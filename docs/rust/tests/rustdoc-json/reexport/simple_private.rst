tests/rustdoc-json/reexport/simple_private.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // edition:2018
#![no_core]
#![feature(no_core)]

// @!has "$.index[*][?(@.name=='inner')]"
mod inner {
    // @set pub_id = "$.index[*][?(@.name=='Public')].id"
    pub struct Public;
}

// @is "$.index[*][?(@.kind=='import')].inner.name" \"Public\"
// @is "$.index[*][?(@.kind=='import')].inner.id" $pub_id
// @set use_id = "$.index[*][?(@.kind=='import')].id"
pub use inner::Public;

// @ismany "$.index[*][?(@.name=='simple_private')].inner.items[*]" $use_id


