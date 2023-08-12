tests/ui/match/match-struct.rs
==============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct S { a: isize }
enum E { C(isize) }

fn main() {
    match (S { a: 1 }) {
        E::C(_) => (),
        //~^ ERROR mismatched types
        //~| expected struct `S`, found enum `E`
        _ => ()
    }
}


