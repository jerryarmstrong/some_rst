tests/ui/panic-runtime/bad-panic-flag2.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags:-C panic
// error-pattern:requires either `unwind` or `abort`

fn main() {}


