tests/rustdoc/issue-67851-hidden.rs
===================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: -Zunstable-options --document-hidden-items

// @has issue_67851_hidden/struct.Hidden.html
#[doc(hidden)]
pub struct Hidden;

// @!has issue_67851_hidden/struct.Private.html
struct Private;


