src/tools/clippy/tests/ui/filter_map_next_fixable.rs
====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-rustfix

#![warn(clippy::all, clippy::pedantic)]
#![allow(unused)]

fn main() {
    let a = ["1", "lol", "3", "NaN", "5"];

    let element: Option<i32> = a.iter().filter_map(|s| s.parse().ok()).next();
    assert_eq!(element, Some(1));
}

#[clippy::msrv = "1.29"]
fn msrv_1_29() {
    let a = ["1", "lol", "3", "NaN", "5"];
    let _: Option<i32> = a.iter().filter_map(|s| s.parse().ok()).next();
}

#[clippy::msrv = "1.30"]
fn msrv_1_30() {
    let a = ["1", "lol", "3", "NaN", "5"];
    let _: Option<i32> = a.iter().filter_map(|s| s.parse().ok()).next();
}


