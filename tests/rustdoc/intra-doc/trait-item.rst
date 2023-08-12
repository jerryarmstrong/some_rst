tests/rustdoc/intra-doc/trait-item.rs
=====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![deny(rustdoc::broken_intra_doc_links)]

/// Link to [S::assoc_fn()]
/// Link to [Default::default()]
// @has trait_item/struct.S.html '//*[@href="struct.S.html#method.assoc_fn"]' 'S::assoc_fn()'
// @has - '//*[@href="{{channel}}/core/default/trait.Default.html#tymethod.default"]' 'Default::default()'
pub struct S;

impl S {
    pub fn assoc_fn() {}
}


