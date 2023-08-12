tests/ui/lexer/lex-bad-char-literals-6.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let x: &str = 'ab';
    //~^ ERROR: character literal may only contain one codepoint
    let y: char = 'cd';
    //~^ ERROR: character literal may only contain one codepoint
    let z = 'ef';
    //~^ ERROR: character literal may only contain one codepoint

    if x == y {}
    if y == z {}  // no error here
    if x == z {}

    let a: usize = "";
    //~^ ERROR: mismatched types
}


