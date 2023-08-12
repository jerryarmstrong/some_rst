tests/ui/consts/const_let_promote.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

use std::cell::Cell;

const X: Option<Cell<i32>> = None;

const Y: Option<Cell<i32>> = {
    let x = None;
    x
};

// Ensure that binding the final value of a `const` to a variable does not affect promotion.
#[allow(unused)]
fn main() {
    let x: &'static _ = &X;
    let y: &'static _ = &Y;
}


