tests/ui/closures/2229_closure_analysis/diagnostics/multilevel-path.rs
======================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // edition:2021

// Test that when a borrow checker diagnostics are emitted, it's as precise
// as the capture by the closure.

#![allow(unused)]

struct Point {
    x: i32,
    y: i32,
}
struct Wrapper {
    p: Point,
}

fn main() {
    let mut w = Wrapper { p: Point { x: 10, y: 10 } };

    let mut c = || {
        w.p.x += 20;
    };

    let py = &mut w.p.x;
    //~^ ERROR: cannot borrow `w.p.x` as mutable more than once at a time
    c();

    *py = 20
}


