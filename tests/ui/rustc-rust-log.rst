tests/ui/rustc-rust-log.rs
==========================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// This test is just checking that we won't ICE if logging is turned
// on; don't bother trying to compare that (copious) output.
//
// dont-check-compiler-stdout
// dont-check-compiler-stderr
// compile-flags: --error-format human
// aux-build: rustc-rust-log-aux.rs
// rustc-env:RUSTC_LOG=debug

fn main() {}


