tests/ui/mir/thir-constparam-temp.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // build-pass

#![feature(adt_const_params)]
#![allow(incomplete_features)]

#[derive(PartialEq, Eq)]
struct Yikes;

impl Yikes {
    fn mut_self(&mut self) {}
}

fn foo<const YIKES: Yikes>() {
    YIKES.mut_self()
    //~^ WARNING taking a mutable reference
}

fn main() {
    foo::<{ Yikes }>()
}


