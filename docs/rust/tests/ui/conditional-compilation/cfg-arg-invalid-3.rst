tests/ui/conditional-compilation/cfg-arg-invalid-3.rs
=====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: --cfg a::b
// error-pattern: invalid `--cfg` argument: `a::b` (argument key must be an identifier)
fn main() {}


