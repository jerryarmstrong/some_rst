tests/ui/unsized-locals/issue-30276-feature-flagged.rs
======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(unsized_locals)]
//~^ WARN the feature `unsized_locals` is incomplete

struct Test([i32]);

fn main() {
    let _x: fn(_) -> Test = Test;
} //~^the size for values of type `[i32]` cannot be known at compilation time


