tests/rustdoc-ui/no-run-flag-error.rs
=====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // test the behavior of the --no-run flag without the --test flag

// compile-flags:-Z unstable-options --no-run --test-args=--test-threads=1
// error-pattern: the `--test` flag must be passed

pub fn f() {}


