tests/rustdoc-json/structs/plain_empty.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // @is "$.index[*][?(@.name=='PlainEmpty')].visibility" \"public\"
// @is "$.index[*][?(@.name=='PlainEmpty')].kind" \"struct\"
// @is "$.index[*][?(@.name=='PlainEmpty')].inner.kind.plain.fields_stripped" false
// @is "$.index[*][?(@.name=='PlainEmpty')].inner.kind.plain.fields" []
pub struct PlainEmpty {}


