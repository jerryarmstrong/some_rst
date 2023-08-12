tests/ui/lexer/lex-bad-char-literals-5.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    static c: char = '\x10\x10';
//~^ ERROR: character literal may only contain one codepoint

fn main() {
    let ch: &str = '\x10\x10';
    //~^ ERROR: character literal may only contain one codepoint
}


