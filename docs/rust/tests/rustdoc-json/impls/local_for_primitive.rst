tests/rustdoc-json/impls/local_for_primitive.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // @set local = "$.index[*][?(@.name=='Local')]"
pub trait Local {}

// @set impl = "$.index[*][?(@.docs=='local for bool')].id"
// @is "$.index[*][?(@.name=='Local')].inner.implementations[*]" $impl
/// local for bool
impl Local for bool {}


