tests/ui/conditional-compilation/cfg-arg-invalid-9.rs
=====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test for missing quotes around value, issue #66450.
// compile-flags: --cfg key=value
// error-pattern: invalid `--cfg` argument: `key=value` (expected `key` or `key="value"`, ensure escaping is appropriate for your shell, try 'key="value"' or key=\"value\")
fn main() {}


