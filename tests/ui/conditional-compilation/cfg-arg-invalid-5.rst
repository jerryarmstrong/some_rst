tests/ui/conditional-compilation/cfg-arg-invalid-5.rs
=====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: --cfg a=10
// error-pattern: invalid `--cfg` argument: `a=10` (argument value must be a string)
fn main() {}


