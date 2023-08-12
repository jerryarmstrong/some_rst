tests/ui/reexport-test-harness-main.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// compile-flags:--test

#![reexport_test_harness_main = "test_main"]

#[cfg(test)]
fn _unused() {
    // should resolve to the entry point function the --test harness
    // creates.
    test_main();
}


