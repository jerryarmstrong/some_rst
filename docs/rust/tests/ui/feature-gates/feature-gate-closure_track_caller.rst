tests/ui/feature-gates/feature-gate-closure_track_caller.rs
===========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(stmt_expr_attributes)]
#![feature(generators)]

fn main() {
    let _closure = #[track_caller] || {}; //~ `#[track_caller]` on closures
    let _generator = #[track_caller] || { yield; }; //~ `#[track_caller]` on closures
}


