tests/rustdoc-ui/check-fail.rs
==============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: -Z unstable-options --check

#![feature(rustdoc_missing_doc_code_examples)]
#![deny(missing_docs)]
#![deny(rustdoc::all)]

//! ```rust,testharness
//~^ ERROR
//! let x = 12;
//! ```

pub fn foo() {}
//~^ ERROR
//~^^ ERROR

/// hello
//~^ ERROR
///
/// ```rust,testharness
/// let x = 12;
/// ```
pub fn bar() {}


