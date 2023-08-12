tests/ui/parser/unsized.rs
==========================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test syntax checks for `type` keyword.

struct S1 for type;
//~^ ERROR expected `where`, `{`, `(`, or `;` after struct name, found keyword `for`

pub fn main() {
}


