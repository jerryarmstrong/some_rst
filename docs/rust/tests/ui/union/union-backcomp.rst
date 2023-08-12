tests/ui/union/union-backcomp.rs
================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// revisions: mirunsafeck thirunsafeck
// [thirunsafeck]compile-flags: -Z thir-unsafeck

#![allow(path_statements)]
#![allow(dead_code)]

macro_rules! union {
    () => (struct S;)
}

union!();

fn union() {}

fn main() {
    union();

    let union = 10;

    union;

    union as u8;

    union U {
        a: u8,
    }
}


