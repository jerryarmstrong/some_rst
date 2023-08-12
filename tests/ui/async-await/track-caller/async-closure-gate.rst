tests/ui/async-await/track-caller/async-closure-gate.rs
=======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // edition:2021

#![feature(async_closure, stmt_expr_attributes)]

fn main() {
    let _ = #[track_caller] async || {
        //~^ ERROR `#[track_caller]` on closures is currently unstable [E0658]
    };
}


