tests/ui/impl-trait/xcrate_simple.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

// aux-build:xcrate.rs

extern crate xcrate;

fn main() {
    xcrate::return_internal_fn()();
}


