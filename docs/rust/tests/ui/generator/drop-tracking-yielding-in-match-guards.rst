tests/ui/generator/drop-tracking-yielding-in-match-guards.rs
============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // build-pass
// edition:2018
// compile-flags: -Zdrop-tracking

#![feature(generators)]

fn main() {
    let _ = static |x: u8| match x {
        y if { yield } == y + 1 => (),
        _ => (),
    };
}


