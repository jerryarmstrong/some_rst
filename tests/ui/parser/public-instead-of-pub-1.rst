tests/ui/parser/public-instead-of-pub-1.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Checks what happens when `public` is used instead of the correct, `pub`
// run-rustfix

public enum Test {
    //~^ ERROR expected one of `!` or `::`, found keyword `enum`
    //~^^ HELP write `pub` instead of `public` to make the item public
    A,
    B,
}

fn main() { }


