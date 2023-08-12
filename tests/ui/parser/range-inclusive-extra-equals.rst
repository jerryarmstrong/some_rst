tests/ui/parser/range-inclusive-extra-equals.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Makes sure that a helpful message is shown when someone mistypes
// an inclusive range as `..==` rather than `..=`. This is an
// easy mistake, because of the resemblance to`==`.
// See #86395 for a bit of background.

pub fn main() {
    if let 1..==3 = 1 {} //~ERROR unexpected `=` after inclusive range
                      //~|HELP use `..=` instead
                      //~|NOTE inclusive ranges end with a single equals sign
}


