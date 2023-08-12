tests/rustdoc/short-docblock-codeblock.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_name = "foo"]

// @count foo/index.html '//*[@class="item-right docblock-short"]' 0

/// ```
/// let x = 12;
/// ```
///
/// Some text.
pub fn foo() {}


