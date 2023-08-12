tests/ui/closures/2229_closure_analysis/capture-analysis-4.rs
=============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // edition:2021

#![feature(rustc_attrs)]

#[derive(Debug)]
struct Child {
    c: String,
    d: String,
}

#[derive(Debug)]
struct Parent {
    b: Child,
}

fn main() {
    let mut a = Parent { b: Child {c: String::new(), d: String::new()} };

    let c = #[rustc_capture_analysis]
    //~^ ERROR: attributes on expressions are experimental
    //~| NOTE: see issue #15701 <https://github.com/rust-lang/rust/issues/15701>
    || {
    //~^ First Pass analysis includes:
    //~| Min Capture analysis includes:
        let _x = a.b;
        //~^ NOTE: Capturing a[(0, 0)] -> ByValue
        //~| NOTE: Min Capture a[(0, 0)] -> ByValue
        println!("{:?}", a.b.c);
        //~^ NOTE: Capturing a[(0, 0),(0, 0)] -> ImmBorrow
    };
}


