tests/ui/parser/removed-syntax-fixed-vec.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    type v = [isize * 3]; //~ ERROR expected one of `!`, `(`, `+`, `::`, `;`, `<`, or `]`, found `*`


