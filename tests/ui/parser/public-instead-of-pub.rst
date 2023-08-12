tests/ui/parser/public-instead-of-pub.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Checks what happens when `public` is used instead of the correct, `pub`
// edition:2018
// run-rustfix
public struct X;
//~^ ERROR expected one of `!` or `::`, found keyword `struct`
//~^^ HELP write `pub` instead of `public` to make the item public

fn main() {}


