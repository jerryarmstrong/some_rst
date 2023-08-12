tests/pretty/top-level-doc-comments.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    /// Some doc comment.
struct X;

// pp-exact

// Test that rust can properly pretty print a doc comment if it's the first line in a file.  some

fn main() { let x = X; }


