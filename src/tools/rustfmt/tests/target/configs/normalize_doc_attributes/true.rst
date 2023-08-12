src/tools/rustfmt/tests/target/configs/normalize_doc_attributes/true.rs
=======================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // rustfmt-normalize_doc_attributes: true
// Normalize doc attributes

//! Example documentation

/// Example item documentation
pub enum Foo {}

///        Lots of space
pub enum Bar {}

///no leading space
pub mod FooBar {}


