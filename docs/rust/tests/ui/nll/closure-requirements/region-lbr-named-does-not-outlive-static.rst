tests/ui/nll/closure-requirements/region-lbr-named-does-not-outlive-static.rs
=============================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Basic test for free regions in the NLL code. This test ought to
// report an error due to a reborrowing constraint. Right now, we get
// a variety of errors from the older, AST-based machinery (notably
// borrowck), and then we get the NLL error at the end.

// compile-flags:-Zverbose

fn foo<'a>(x: &'a u32) -> &'static u32 {
    &*x
        //~^ ERROR
}

fn main() { }


