tests/ui/parser/suggest-semicolon-before-array.rs
=================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-rustfix
#![allow(dead_code)]

fn foo() {}

fn bar() -> [u8; 2] {
    foo()
    [1, 3] //~ ERROR expected `;`, found `[`
}

fn main() {}


