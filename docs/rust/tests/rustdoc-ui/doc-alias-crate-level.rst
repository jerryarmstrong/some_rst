tests/rustdoc-ui/doc-alias-crate-level.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![doc(alias = "crate-level-not-working")] //~ ERROR

#[doc(alias = "shouldn't work!")] //~ ERROR
pub fn foo() {}


