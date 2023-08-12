src/tools/rustfmt/tests/source/normalize_multiline_doc_attribute.rs
===================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // rustfmt-unstable: true
// rustfmt-normalize_doc_attributes: true

#[doc = "This comment
is split
on multiple lines"]
fn foo() {}

#[doc = " B1"]
#[doc = ""]
#[doc = " A1"]
fn bar() {}


