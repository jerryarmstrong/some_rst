tests/ui/issues/issue-948.rs
============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-fail
// error-pattern:beep boop
// ignore-emscripten no processes

#![allow(unused_variables)]

struct Point {
    x: isize,
    y: isize,
}

fn main() {
    let origin = Point { x: 0, y: 0 };
    let f: Point = Point { x: (panic!("beep boop")), ..origin };
}


