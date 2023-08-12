tests/ui/parser/keyword-loop-as-identifier.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // This file was auto-generated using 'src/etc/generate-keyword-tests.py loop'

fn main() {
    let loop = "foo"; //~ error: expected identifier, found keyword `loop`
}


