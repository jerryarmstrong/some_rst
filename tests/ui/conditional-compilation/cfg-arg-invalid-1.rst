tests/ui/conditional-compilation/cfg-arg-invalid-1.rs
=====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: --cfg a(b=c)
// error-pattern: invalid `--cfg` argument: `a(b=c)` (expected `key` or `key="value"`, ensure escaping is appropriate for your shell, try 'key="value"' or key=\"value\")
fn main() {}


