tests/ui/parser/bounds-lifetime-where-1.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    type A where 'a; //~ ERROR expected `:`, found `;`

fn main() {}


