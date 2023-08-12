tests/ui/panics/unique-panic.rs
===============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-fail
// error-pattern: panic
// for some reason, fails to match error string on
// wasm32-unknown-unknown with stripped debuginfo and symbols,
// so don't strip it
// compile-flags:-Cstrip=none

fn main() {
    Box::new(panic!());
}


