tests/ui/impossible_range.rs
============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-rustfix
// Make sure that invalid ranges generate an error during parsing, not an ICE

#![allow(path_statements)]

pub fn main() {
    ..;
    0..;
    ..1;
    0..1;
    ..=; //~ERROR inclusive range with no end
         //~^HELP use `..` instead
}

fn _foo1() {
    ..=1;
    0..=1;
    0..=; //~ERROR inclusive range with no end
          //~^HELP use `..` instead
}


