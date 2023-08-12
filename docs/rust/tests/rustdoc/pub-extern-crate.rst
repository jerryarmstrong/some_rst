tests/rustdoc/pub-extern-crate.rs
=================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // aux-build:pub-extern-crate.rs

// @has pub_extern_crate/index.html
// @!has - '//code' 'pub extern crate inner'
// @has - '//a/@href' 'inner/index.html'
// @has pub_extern_crate/inner/index.html
// @has pub_extern_crate/inner/struct.SomeStruct.html
#[doc(inline)]
pub extern crate inner;


