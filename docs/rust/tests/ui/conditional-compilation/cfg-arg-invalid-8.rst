tests/ui/conditional-compilation/cfg-arg-invalid-8.rs
=====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: --cfg )
// error-pattern: invalid `--cfg` argument: `)` (expected `key` or `key="value"`)
fn main() {}


