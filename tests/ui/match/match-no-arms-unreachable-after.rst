tests/ui/match/match-no-arms-unreachable-after.rs
=================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![allow(warnings)]
#![deny(unreachable_code)]

enum Void { }

fn foo(v: Void) {
    match v { }
    let x = 2; //~ ERROR unreachable
}

fn main() {
}


