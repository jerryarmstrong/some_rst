tests/rustdoc/primitive-slice-auto-trait.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: --crate-type lib --edition 2018

#![crate_name = "foo"]
#![feature(rustdoc_internals)]

// @has foo/primitive.slice.html '//a[@class="primitive"]' 'slice'
// @has - '//h1' 'Primitive Type slice'
// @has - '//section[@id="main-content"]//div[@class="docblock"]//p' 'this is a test!'
// @has - '//h2[@id="synthetic-implementations"]' 'Auto Trait Implementations'
// @has - '//div[@id="synthetic-implementations-list"]//h3' 'impl<T> Send for [T]where T: Send'
// @has - '//div[@id="synthetic-implementations-list"]//h3' 'impl<T> Sync for [T]where T: Sync'
#[doc(primitive = "slice")]
/// this is a test!
mod slice_prim {}


