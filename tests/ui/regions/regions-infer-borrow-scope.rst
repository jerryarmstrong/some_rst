tests/ui/regions/regions-infer-borrow-scope.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(dead_code)]

struct Point {x: isize, y: isize}

fn x_coord(p: &Point) -> &isize {
    return &p.x;
}

pub fn main() {
    let p: Box<_> = Box::new(Point {x: 3, y: 4});
    let xc = x_coord(&*p);
    assert_eq!(*xc, 3);
}


