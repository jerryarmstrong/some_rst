tests/ui/parser/lifetime-semicolon.rs
=====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-rustfix
#![allow(unused)]
struct Foo<'a, 'b> {
    a: &'a &'b i32
}

fn foo<'a, 'b>(_x: &mut Foo<'a; 'b>) {}
//~^ ERROR expected one of `,` or `>`, found `;`

fn main() {}


