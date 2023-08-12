tests/ui/closures/2229_closure_analysis/run_pass/multilevel-path-1.rs
=====================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // edition:2021
// run-pass

// Test that closures can capture paths that are more precise than just one level
// from the root variable.
//
// If the closures can handle such precision we should be able to mutate one path in the closure
// while being able to mutate another path outside the closure, where the two paths are disjoint
// after applying two projections on the root variable.

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

    // `c` only captures `w.p.x`, therefore it's safe to mutate `w.p.y`.
    let py = &mut w.p.y;
    c();

    *py = 20
}


