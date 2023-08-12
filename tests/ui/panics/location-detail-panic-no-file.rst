tests/ui/panics/location-detail-panic-no-file.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-fail
// check-run-results
// compile-flags: -Zlocation-detail=line,column
// exec-env:RUST_BACKTRACE=0

fn main() {
    panic!("file-redacted");
}


