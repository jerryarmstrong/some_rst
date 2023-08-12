tests/ui/parser/keyword-break-as-identifier.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // This file was auto-generated using 'src/etc/generate-keyword-tests.py break'

fn main() {
    let break = "foo"; //~ error: expected identifier, found keyword `break`
}


