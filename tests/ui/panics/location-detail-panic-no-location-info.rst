tests/ui/panics/location-detail-panic-no-location-info.rs
=========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-fail
// check-run-results
// compile-flags: -Zlocation-detail=none
// exec-env:RUST_BACKTRACE=0

fn main() {
    panic!("no location info");
}


