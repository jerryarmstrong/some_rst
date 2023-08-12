tests/ui/parser/default-unmatched.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    mod foo {
    default!(); // OK.
    default do
    //~^ ERROR `default` is not followed by an item
    //~| ERROR expected item, found reserved keyword `do`
}


