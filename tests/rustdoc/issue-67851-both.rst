tests/rustdoc/issue-67851-both.rs
=================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: -Zunstable-options --document-private-items --document-hidden-items

// @has issue_67851_both/struct.Hidden.html
#[doc(hidden)]
pub struct Hidden;

// @has issue_67851_both/struct.Private.html
struct Private;


