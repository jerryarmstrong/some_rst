tests/ui/hygiene/panic-location.rs
==================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-fail
// check-run-results
// exec-env:RUST_BACKTRACE=0
//
// Regression test for issue #70963
// The captured stderr from this test reports a location
// inside `VecDeque::with_capacity`, instead of `<::core::macros::panic macros>`
fn main() {
    std::collections::VecDeque::<String>::with_capacity(!0);
}


