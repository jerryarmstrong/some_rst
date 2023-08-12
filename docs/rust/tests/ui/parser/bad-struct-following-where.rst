tests/ui/parser/bad-struct-following-where.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct A where T: Sized !
//~^ ERROR expected `{` after struct name, found


