tests/ui/lexer/lex-bad-octal-literal.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    0o18; //~ ERROR invalid digit for a base 8 literal
    0o1234_9_5670;  //~ ERROR invalid digit for a base 8 literal
}


