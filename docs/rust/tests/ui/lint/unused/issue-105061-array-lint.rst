tests/ui/lint/unused/issue-105061-array-lint.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![warn(unused)]
#![deny(warnings)]

fn main() {
    let _x: ([u32; 3]); //~ ERROR unnecessary parentheses around type
    let _y: [u8; (3)]; //~ ERROR unnecessary parentheses around const expression
    let _z: ([u8; (3)]);
    //~^ ERROR unnecessary parentheses around const expression
    //~| ERROR unnecessary parentheses around type

}


