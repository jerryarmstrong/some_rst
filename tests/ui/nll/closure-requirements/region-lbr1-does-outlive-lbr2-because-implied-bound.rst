tests/ui/nll/closure-requirements/region-lbr1-does-outlive-lbr2-because-implied-bound.rs
========================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Basic test for free regions in the NLL code. This test does not
// report an error because of the (implied) bound that `'b: 'a`.

// check-pass
// compile-flags:-Zverbose

fn foo<'a, 'b>(x: &'a &'b u32) -> &'a u32 {
    &**x
}

fn main() {}


