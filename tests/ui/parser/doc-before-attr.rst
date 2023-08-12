tests/ui/parser/doc-before-attr.rs
==================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {}

/// hi
#[derive(Debug)] //~ERROR expected item after attributes


