tests/ui/suggestions/type-mismatch-byte-literal.rs
==================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Tests that a suggestion is issued for type mismatch errors when a
// u8 is expected and a char literal which is ASCII is supplied.

fn foo(_t: u8) {}

fn main() {
    let _x: u8 = 'X';
    //~^ ERROR: mismatched types [E0308]
    //~| HELP: if you meant to write a byte literal, prefix with `b`

    foo('#');
    //~^ ERROR: mismatched types [E0308]
    //~| HELP: if you meant to write a byte literal, prefix with `b`

    // Do not issue the suggestion if the char literal isn't ASCII
    let _t: u8 = '€';
    //~^ ERROR: mismatched types [E0308]
}


