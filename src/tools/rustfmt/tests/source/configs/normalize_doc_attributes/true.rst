src/tools/rustfmt/tests/source/configs/normalize_doc_attributes/true.rs
=======================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // rustfmt-normalize_doc_attributes: true
// Normalize doc attributes

#![doc = " Example documentation"]

#[doc = " Example item documentation"]
pub enum Foo {}

#[doc = "        Lots of space"]
pub enum Bar {}

#[doc = "no leading space"]
pub mod FooBar {}


