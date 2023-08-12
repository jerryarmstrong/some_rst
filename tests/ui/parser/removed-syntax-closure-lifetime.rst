tests/ui/parser/removed-syntax-closure-lifetime.rs
==================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    type closure = Box<lt/fn()>;
//~^ ERROR expected one of `!`, `(`, `+`, `,`, `::`, `:`, `<`, `=`, or `>`, found `/`


