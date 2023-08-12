tests/rustdoc/issue-67851-neither.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // @!has issue_67851_neither/struct.Hidden.html
#[doc(hidden)]
pub struct Hidden;

// @!has issue_67851_neither/struct.Private.html
struct Private;


