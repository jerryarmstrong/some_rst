tests/rustdoc/inline_cross/auxiliary/macros.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(staged_api)]
#![stable(feature = "rust1", since = "1.0.0")]

/// docs for my_macro
#[unstable(feature = "macro_test", issue = "none")]
#[deprecated(since = "1.2.3", note = "text")]
#[macro_export]
macro_rules! my_macro {
    () => {};
}


