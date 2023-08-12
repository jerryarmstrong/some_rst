tests/rustdoc/doc-notable_trait-slice.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(doc_notable_trait)]

#[doc(notable_trait)]
pub trait SomeTrait {}

pub struct SomeStruct;
pub struct OtherStruct;
impl SomeTrait for &[SomeStruct] {}

// @has doc_notable_trait_slice/fn.bare_fn_matches.html
// @snapshot bare_fn_matches - '//script[@id="notable-traits-data"]'
pub fn bare_fn_matches() -> &'static [SomeStruct] {
    &[]
}

// @has doc_notable_trait_slice/fn.bare_fn_no_matches.html
// @count - '//script[@id="notable-traits-data"]' 0
pub fn bare_fn_no_matches() -> &'static [OtherStruct] {
    &[]
}


