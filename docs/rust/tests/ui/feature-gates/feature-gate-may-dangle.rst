tests/ui/feature-gates/feature-gate-may-dangle.rs
=================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // gate-test-dropck_eyepatch

// Check that `may_dangle` is rejected if `dropck_eyepatch` feature gate is absent.

struct Pt<A>(A);
unsafe impl<#[may_dangle] A> Drop for Pt<A> {
    //~^ ERROR `may_dangle` has unstable semantics and may be removed in the future
    fn drop(&mut self) { }
}

fn main() {}


