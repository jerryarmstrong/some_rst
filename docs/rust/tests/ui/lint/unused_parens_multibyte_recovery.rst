tests/ui/lint/unused_parens_multibyte_recovery.rs
=================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // ignore-tidy-trailing-newlines
//
// error-pattern: this file contains an unclosed delimiter
// error-pattern: this file contains an unclosed delimiter
// error-pattern: this file contains an unclosed delimiter
// error-pattern: format argument must be a string literal
//
// Verify that unused parens lint does not try to create a span
// which points in the middle of a multibyte character.

fn f(){(print!(á

