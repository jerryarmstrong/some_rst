tests/pretty/block-comment-trailing-whitespace2.rs
==================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: --crate-type=lib

// pp-exact
fn f() {} /*
          The next line should not be indented.

          That one. It shouldn't have been indented.
          */


