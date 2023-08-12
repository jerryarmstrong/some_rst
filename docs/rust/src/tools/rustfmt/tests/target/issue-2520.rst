src/tools/rustfmt/tests/target/issue-2520.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // rustfmt-normalize_comments: true
// rustfmt-format_code_in_doc_comments: true

//! ```rust
//! println!("hello, world");
//! ```

#![deny(missing_docs)]

//! ```rust
//! println!("hello, world");

#![deny(missing_docs)]


