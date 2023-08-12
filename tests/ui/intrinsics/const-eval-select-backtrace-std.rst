tests/ui/intrinsics/const-eval-select-backtrace-std.rs
======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // See issue #100696.
// run-fail
// check-run-results
// exec-env:RUST_BACKTRACE=0
fn main() {
    &""[1..];
}


