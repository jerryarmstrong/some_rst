tests/ui/lint/issue-103435-extra-parentheses.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-rustfix
#![deny(unused_parens)]

fn main() {
    if let(Some(_))= Some(1) {}
    //~^ ERROR unnecessary parentheses around pattern

    for(_x)in 1..10 {}
    //~^ ERROR unnecessary parentheses around pattern

    if(2 == 1){}
    //~^ ERROR unnecessary parentheses around `if` condition

    // reported by parser
    for(_x in 1..10){}
    //~^ ERROR expected one of
    //~| ERROR unexpected parentheses surrounding
}


