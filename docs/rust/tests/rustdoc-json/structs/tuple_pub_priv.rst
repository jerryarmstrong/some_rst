tests/rustdoc-json/structs/tuple_pub_priv.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    pub struct Demo(
    i32,
    /// field
    pub i32,
    #[doc(hidden)] i32,
);

// @set field = "$.index[*][?(@.docs=='field')].id"

// @is    "$.index[*][?(@.name=='Demo')].inner.kind.tuple[0]" null
// @is    "$.index[*][?(@.name=='Demo')].inner.kind.tuple[1]" $field
// @is    "$.index[*][?(@.name=='Demo')].inner.kind.tuple[2]" null
// @count "$.index[*][?(@.name=='Demo')].inner.kind.tuple[*]" 3


