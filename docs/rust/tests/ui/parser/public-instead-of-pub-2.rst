tests/ui/parser/public-instead-of-pub-2.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Checks what happens when `public` is used instead of the correct, `pub`
// Won't give help message for this case

public let x = 1;
//~^ ERROR expected one of `!` or `::`, found keyword `let`

fn main() { }


