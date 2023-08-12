tests/ui/parser/keyword-as-as-identifier.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // This file was auto-generated using 'src/etc/generate-keyword-tests.py as'

fn main() {
    let as = "foo"; //~ error: expected identifier, found keyword `as`
}


