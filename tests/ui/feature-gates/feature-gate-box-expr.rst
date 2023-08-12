tests/ui/feature-gates/feature-gate-box-expr.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // gate-test-box_syntax

// Check that `box EXPR` is feature-gated.
//
// See also feature-gate-placement-expr.rs
//
// (Note that the two tests are separated since the checks appear to
// be performed at distinct phases, with an abort_if_errors call
// separating them.)

fn main() {
    let x = box 'c'; //~ ERROR box expression syntax is experimental
    println!("x: {}", x);
}


