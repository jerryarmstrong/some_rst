tests/rustdoc-ui/private-doc-test.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

#![deny(rustdoc::private_doc_tests)]

mod foo {
    /// private doc test
    ///
    /// ```ignore (used for testing ignored doc tests)
    /// assert!(false);
    /// ```
    fn bar() {}
}


