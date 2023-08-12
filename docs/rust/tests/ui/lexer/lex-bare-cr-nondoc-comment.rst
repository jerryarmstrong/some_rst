tests/ui/lexer/lex-bare-cr-nondoc-comment.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// ignore-tidy-cr

// nondoc comment with bare CR: ''
//// nondoc comment with bare CR: ''
/* block nondoc comment with bare CR: '' */

fn main() {
}


