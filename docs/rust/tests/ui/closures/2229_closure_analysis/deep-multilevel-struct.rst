tests/ui/closures/2229_closure_analysis/deep-multilevel-struct.rs
=================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // edition:2021

#![feature(rustc_attrs)]
#![allow(unused)]

#[derive(Debug)]
struct Point {
    x: i32,
    y: i32,
}
#[derive(Debug)]
struct Line {
    p: Point,
    q: Point
}
#[derive(Debug)]
struct Plane {
    a: Line,
    b: Line,
}

fn main() {
    let mut p = Plane {
        a: Line {
            p: Point { x: 1,y: 2 },
            q: Point { x: 3,y: 4 },
        },
        b: Line {
            p: Point { x: 1,y: 2 },
            q: Point { x: 3,y: 4 },
        }
    };

    let c = #[rustc_capture_analysis]
    //~^ ERROR: attributes on expressions are experimental
    //~| NOTE: see issue #15701 <https://github.com/rust-lang/rust/issues/15701>
    || {
    //~^ ERROR: First Pass analysis includes:
    //~| ERROR: Min Capture analysis includes:
        let x = &p.a.p.x;
        //~^ NOTE: Capturing p[(0, 0),(0, 0),(0, 0)] -> ImmBorrow
        p.b.q.y = 9;
        //~^ NOTE: Capturing p[(1, 0),(1, 0),(1, 0)] -> MutBorrow
        //~| NOTE: p[] captured as MutBorrow here
        println!("{:?}", p);
        //~^ NOTE: Capturing p[] -> ImmBorrow
        //~| NOTE: Min Capture p[] -> MutBorrow
        //~| NOTE: p[] used here
    };
}


