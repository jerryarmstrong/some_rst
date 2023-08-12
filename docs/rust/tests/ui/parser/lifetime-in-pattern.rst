tests/ui/parser/lifetime-in-pattern.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn test(&'a str) {
    //~^ ERROR unexpected lifetime `'a` in pattern
    //~| ERROR expected one of `:`, `@`, or `|`, found `)`
}

fn main() {
}


