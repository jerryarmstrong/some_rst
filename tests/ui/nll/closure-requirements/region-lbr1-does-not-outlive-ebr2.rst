tests/ui/nll/closure-requirements/region-lbr1-does-not-outlive-ebr2.rs
======================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Basic test for free regions in the NLL code. This test ought to
// report an error due to a reborrowing constraint. Right now, we get
// a variety of errors from the older, AST-based machinery (notably
// borrowck), and then we get the NLL error at the end.

// compile-flags:-Zverbose

fn foo<'a, 'b>(x: &'a u32, y: &'b u32) -> &'b u32 {
    &*x
    //~^ ERROR lifetime may not live long enough
}

fn main() {}


