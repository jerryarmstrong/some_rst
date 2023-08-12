tests/ui/unsafe/union_wild_or_wild.rs
=====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
// revisions: mir thir
// [thir]compile-flags: -Z thir-unsafeck

union X { a: i8 }

fn main() {
    let x = X { a: 5 };
    match x {
        X { a: _ | _ } => {},
    }
}


