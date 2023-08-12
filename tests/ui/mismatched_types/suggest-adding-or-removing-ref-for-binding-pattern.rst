tests/ui/mismatched_types/suggest-adding-or-removing-ref-for-binding-pattern.rs
===============================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-rustfix
#![allow(dead_code, unused_variables)]

fn main() {
    enum Blah {
        A(isize, isize, usize),
        B(isize, usize),
    }

    match Blah::A(1, 1, 2) {
        Blah::A(_, x, ref y) | Blah::B(x, y) => {}
        //~^ ERROR mismatched types
        //~| ERROR variable `y` is bound inconsistently across alternatives separated by `|`
    }

    match Blah::A(1, 1, 2) {
        Blah::A(_, x, y) | Blah::B(x, ref y) => {}
        //~^ ERROR mismatched types
        //~| variable `y` is bound inconsistently across alternatives separated by `|`
    }
}


