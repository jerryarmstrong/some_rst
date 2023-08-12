tests/ui/parser/keyword-trait-as-identifier.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // This file was auto-generated using 'src/etc/generate-keyword-tests.py trait'

fn main() {
    let trait = "foo"; //~ error: expected identifier, found keyword `trait`
}


