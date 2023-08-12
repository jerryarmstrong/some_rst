tests/rustdoc-json/structs/tuple.rs
===================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // @is "$.index[*][?(@.name=='Tuple')].visibility" \"public\"
// @is "$.index[*][?(@.name=='Tuple')].kind" \"struct\"
// @is "$.index[*][?(@.name=='Tuple')].inner.kind.tuple" '[null, null]'
pub struct Tuple(u32, String);


