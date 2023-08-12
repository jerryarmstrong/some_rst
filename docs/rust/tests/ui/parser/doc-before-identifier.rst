tests/ui/parser/doc-before-identifier.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn /// document
foo() {}
//~^^ ERROR expected identifier, found doc comment `/// document`

fn main() {
    foo();
}


