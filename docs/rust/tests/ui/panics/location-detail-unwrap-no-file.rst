tests/ui/panics/location-detail-unwrap-no-file.rs
=================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-fail
// check-run-results
// compile-flags: -Copt-level=0 -Zlocation-detail=line,column
// exec-env:RUST_BACKTRACE=0

fn main() {
    let opt: Option<u32> = None;
    opt.unwrap();
}


