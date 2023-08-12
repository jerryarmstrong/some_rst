tests/rustdoc-ui/public-reexported-item-doc-test.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

#![deny(rustdoc::private_doc_tests)]

pub fn foo() {}

mod private {
    /// re-exported doc test
    ///
    /// ```
    /// assert!(true);
    /// ```
    pub fn bar() {}
}

pub use private::bar;


