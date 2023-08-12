src/tools/rustfmt/tests/target/issue-1703.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // rustfmt should not remove doc comments or comments inside attributes.

/**
This function has a block doc comment.
 */
fn test_function() {}

#[foo /* do not remove this! */]
fn foo() {}


