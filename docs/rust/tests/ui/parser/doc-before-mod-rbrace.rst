tests/ui/parser/doc-before-mod-rbrace.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    mod Foo {
    /// document
    //~^ ERROR expected item after doc comment
}

fn main() {}


