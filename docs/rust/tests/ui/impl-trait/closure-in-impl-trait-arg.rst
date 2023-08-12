tests/ui/impl-trait/closure-in-impl-trait-arg.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(unused_must_use)]
fn bug(_: impl Iterator<Item = [(); { |x: u32| { x }; 4 }]>) {}

fn main() {
    bug(std::iter::empty());
}


