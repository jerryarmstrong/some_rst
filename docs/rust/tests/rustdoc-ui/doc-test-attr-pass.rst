tests/rustdoc-ui/doc-test-attr-pass.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

#![crate_type = "lib"]
#![deny(invalid_doc_attributes)]
#![doc(test(no_crate_inject))]
#![doc(test(attr(deny(warnings))))]

pub fn foo() {}


