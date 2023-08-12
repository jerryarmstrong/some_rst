tests/ui/parser/removed-syntax-uniq-mut-ty.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    type mut_box = Box<mut isize>;
//~^ ERROR expected one of `>`, a const expression, lifetime, or type, found keyword `mut`


