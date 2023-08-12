src/tools/rustfmt/tests/target/normalize_multiline_doc_attribute.rs
===================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // rustfmt-unstable: true
// rustfmt-normalize_doc_attributes: true

///This comment
///is split
///on multiple lines
fn foo() {}

/// B1
///
/// A1
fn bar() {}


