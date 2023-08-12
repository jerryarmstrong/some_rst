tests/ui/panic-runtime/want-abort-got-unwind2.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // build-fail
// dont-check-compiler-stderr
// error-pattern:is not compiled with this crate's panic strategy `abort`
// aux-build:panic-runtime-unwind.rs
// aux-build:wants-panic-runtime-unwind.rs
// compile-flags:-C panic=abort

extern crate wants_panic_runtime_unwind;

fn main() {}


