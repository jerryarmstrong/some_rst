tests/ui/parser/range_inclusive.rs
==================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-rustfix
// Make sure that inclusive ranges with no end point don't parse.

pub fn main() {
    for _ in 1..= {} //~ERROR inclusive range with no end
                     //~^HELP use `..` instead
}


