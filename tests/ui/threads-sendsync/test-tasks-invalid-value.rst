tests/ui/threads-sendsync/test-tasks-invalid-value.rs
=====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // This checks that RUST_TEST_THREADS not being 1, 2, ... is detected
// properly.

// run-fail
// error-pattern:should be a positive integer
// compile-flags: --test
// exec-env:RUST_TEST_THREADS=foo
// ignore-emscripten

#[test]
fn do_nothing() {}


