tests/ui/generator/static-reference-across-yield.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // build-pass
#![feature(generators)]

static A: [i32; 5] = [1, 2, 3, 4, 5];

fn main() {
    static || {
        let u = A[{yield; 1}];
    };
    static || {
        match A {
            i if { yield; true } => (),
            _ => (),
        }
    };
}


