tests/ui/parser/do-not-suggest-semicolon-before-array.rs
========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn foo() {}

fn bar() -> [u8; 2] {
    foo()
    [1, 3) //~ ERROR expected one of `.`, `?`, `]`, or an operator, found `,`
}

fn main() {}


