src/tools/clippy/tests/ui/fn_address_comparisons.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use std::fmt::Debug;
use std::ptr;
use std::rc::Rc;
use std::sync::Arc;

fn a() {}

#[warn(clippy::fn_address_comparisons)]
fn main() {
    type F = fn();
    let f: F = a;
    let g: F = f;

    // These should fail:
    let _ = f == a;
    let _ = f != a;

    // These should be fine:
    let _ = f == g;
}


