tests/ui/lexer/lex-bad-char-literals-3.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    static c: char = '●●';
//~^ ERROR: character literal may only contain one codepoint

fn main() {
    let ch: &str = '●●';
    //~^ ERROR: character literal may only contain one codepoint
}


