tests/pretty/block-comment-multiple-asterisks.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: --crate-type=lib

// pp-exact
/***
More than two asterisks means that it isn't a doc comment.
*/


