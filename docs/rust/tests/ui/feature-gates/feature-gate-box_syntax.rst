tests/ui/feature-gates/feature-gate-box_syntax.rs
=================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test that the use of the box syntax is gated by `box_syntax` feature gate.

fn main() {
    let x = box 3;
    //~^ ERROR box expression syntax is experimental; you can call `Box::new` instead
}


