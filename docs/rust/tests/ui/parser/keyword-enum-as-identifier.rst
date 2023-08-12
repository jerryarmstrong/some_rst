tests/ui/parser/keyword-enum-as-identifier.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // This file was auto-generated using 'src/etc/generate-keyword-tests.py enum'

fn main() {
    let enum = "foo"; //~ error: expected identifier, found keyword `enum`
}


