tests/rustdoc-ui/private-public-item-doc-test.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![deny(rustdoc::private_doc_tests)]

mod foo {
    /// private doc test
    ///
    /// ```
    /// assert!(false);
    /// ```
    //~^^^^^ ERROR documentation test in private item
    pub fn bar() {}
}


