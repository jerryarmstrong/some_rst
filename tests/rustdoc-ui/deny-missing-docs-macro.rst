tests/rustdoc-ui/deny-missing-docs-macro.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    //! foo

#![deny(missing_docs)]

#[macro_export]
macro_rules! foo { //~ ERROR
    () => {}
}


