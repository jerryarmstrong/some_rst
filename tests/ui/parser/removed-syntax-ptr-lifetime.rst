tests/ui/parser/removed-syntax-ptr-lifetime.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    type bptr = &lifetime/isize; //~ ERROR expected one of `!`, `(`, `::`, `;`, `<`, or `where`, found `/`


