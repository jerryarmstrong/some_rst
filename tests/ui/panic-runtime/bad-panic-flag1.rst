tests/ui/panic-runtime/bad-panic-flag1.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags:-C panic=foo
// error-pattern:either `unwind` or `abort` was expected

fn main() {}


