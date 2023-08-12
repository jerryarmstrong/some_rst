tests/rustdoc/issue-67851-private.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: --document-private-items

// @!has issue_67851_private/struct.Hidden.html
#[doc(hidden)]
pub struct Hidden;

// @has issue_67851_private/struct.Private.html
struct Private;


