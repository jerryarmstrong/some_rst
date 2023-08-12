tests/ui/parser/keyword-in-as-identifier.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // This file was auto-generated using 'src/etc/generate-keyword-tests.py in'

fn main() {
    let in = "foo"; //~ error: expected pattern, found keyword `in`
}


