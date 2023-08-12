tests/ui/parser/empty-impl-semicolon.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct Foo;
impl Foo; //~ ERROR expected `{}`, found `;`

fn main() {}


