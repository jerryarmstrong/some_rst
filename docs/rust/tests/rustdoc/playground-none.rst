tests/rustdoc/playground-none.rs
================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_name = "foo"]

//! module docs
//!
//! ```
//! println!("Hello, world!");
//! ```

// @!has foo/index.html '//a[@class="test-arrow"]' "Run"


