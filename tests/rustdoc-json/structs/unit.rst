tests/rustdoc-json/structs/unit.rs
==================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // @is "$.index[*][?(@.name=='Unit')].visibility" \"public\"
// @is "$.index[*][?(@.name=='Unit')].kind" \"struct\"
// @is "$.index[*][?(@.name=='Unit')].inner.kind" \"unit\"
pub struct Unit;


