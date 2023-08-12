tests/ui/conditional-compilation/cfg-arg-invalid-7.rs
=====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Regression test for issue #89358.

// compile-flags: --cfg a"
// error-pattern: unterminated double quote string
// error-pattern: this error occurred on the command line


