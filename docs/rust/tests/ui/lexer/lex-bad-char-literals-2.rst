tests/ui/lexer/lex-bad-char-literals-2.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // This test needs to the last one appearing in this file as it kills the parser
static c: char =
    'nope' //~ ERROR: character literal may only contain one codepoint
;

fn main() {}


