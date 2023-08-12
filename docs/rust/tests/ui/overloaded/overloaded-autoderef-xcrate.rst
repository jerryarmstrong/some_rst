tests/ui/overloaded/overloaded-autoderef-xcrate.rs
==================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// aux-build:overloaded_autoderef_xc.rs


extern crate overloaded_autoderef_xc;

fn main() {
    assert!(overloaded_autoderef_xc::check(5, 5));
}


