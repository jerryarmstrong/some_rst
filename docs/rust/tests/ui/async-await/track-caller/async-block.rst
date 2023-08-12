tests/ui/async-await/track-caller/async-block.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // edition:2021

#![feature(closure_track_caller, stmt_expr_attributes)]

fn main() {
    let _ = #[track_caller] async {
        //~^ ERROR attribute should be applied to a function definition [E0739]
    };
}


