tests/rustdoc/inline_cross/add-docs.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // aux-build:add-docs.rs

extern crate inner;


// @has add_docs/struct.MyStruct.html
// @hasraw add_docs/struct.MyStruct.html "Doc comment from ‘pub use’, Doc comment from definition"
/// Doc comment from 'pub use',
pub use inner::MyStruct;


