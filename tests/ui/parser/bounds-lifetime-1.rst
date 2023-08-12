tests/ui/parser/bounds-lifetime-1.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    type A = for<'a 'b> fn(); //~ ERROR expected one of `,`, `:`, or `>`, found `'b`

fn main() {}


