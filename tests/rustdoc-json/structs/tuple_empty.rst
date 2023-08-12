tests/rustdoc-json/structs/tuple_empty.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // @is "$.index[*][?(@.name=='TupleUnit')].inner.kind.tuple" []
pub struct TupleUnit();


