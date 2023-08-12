tests/ui/parser/use-as-where-use-ends-with-mod-sep.rs
=====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use std::any:: as foo; //~ ERROR expected identifier, found keyword `as`
//~^ ERROR: expected one of `::`, `;`, or `as`, found `foo`


