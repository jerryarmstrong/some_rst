tests/ui/lexer/lex-bad-char-literals-7.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let _: char = '';
    //~^ ERROR: empty character literal
    let _: char = '\u{}';
    //~^ ERROR: empty unicode escape

    // Next two are OK, but may befool error recovery
    let _ = '/';
    let _ = b'/';

    let _ = ' hello // here's a comment
    //~^ ERROR: unterminated character literal
}


