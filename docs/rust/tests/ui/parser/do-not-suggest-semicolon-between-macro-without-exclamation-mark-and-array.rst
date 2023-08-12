tests/ui/parser/do-not-suggest-semicolon-between-macro-without-exclamation-mark-and-array.rs
============================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let _x = vec[1, 2, 3]; //~ ERROR expected one of `.`, `?`, `]`, or an operator
}


