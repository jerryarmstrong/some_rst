tests/ui/coherence/coherence-overlap-all-t-and-tuple.rs
=======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Check that we detect an overlap here in the case where:
//
//    for some type X:
//      T = (X,)
//      T11 = X, U11 = X
//
// Seems pretty basic, but then there was issue #24241. :)

trait From<U> {
    fn foo() {}
}

impl <T> From<T> for T {
}

impl <T11, U11> From<(U11,)> for (T11,) {
//~^ ERROR E0119
}

fn main() { }


